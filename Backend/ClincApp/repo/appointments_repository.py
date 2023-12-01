from ClincApp.models import Appointments
from rest_framework.parsers import JSONParser
import json
from ClincApp.serializers import AppointmentsSerializer, CreateAppointmentsSerializer
#from ClincApp.repo.appointments_repository import
class AppointmentsRepository:
    def get_all_appointments(self):
        appointments = Appointments.objects.all()
        appointments_serializer = AppointmentsSerializer(appointments, many=True)
        return appointments_serializer

    def get_appointment_by_appointment_id(self, app_id):
        appointment =  Appointments.objects.get(appointment_id = app_id)
        return appointment

    def get_appointment_by_patient_id(self, p_id):
        appointments_qs = Appointments.objects.select_related("slot").filter(patient_id__exact = p_id)
        #appointments = Appointments.objects.get(patient_id = p_id, many= True)
        #appointments_serializer = AppointmentsSerializer(appointments, many= True)
        #return appointments_serializer
        return list(appointments_qs.values())

    def get_current_appointment_id(self):
        appointments = Appointments.objects.all().order_by("-appointment_id")[0]
        id = int(appointments.appointment_id)+1
        return id



    def create_appointment(self, request):
        appointment_serializer = AppointmentsSerializer(data= request, many =False)
        if appointment_serializer.is_valid():
            print ("data in serializer = {}".format(appointment_serializer.validated_data))
            appointment_serializer.save()
            return True
        else:
            #print ("data in appointment = {}, {}, {}".format(appointment.appointment_id, appointment.slot, appointment.patient))
            print ("data in serializer = {}".format(appointment_serializer.data))
            return False

    def get_patient_reserved_slot_ids(self, patient_id):
        patient_appointments_qs = Appointments.objects.filter(patient_id__exact = patient_id)
        patient_appointments = list(patient_appointments_qs.values())
        slot_ids = []
        for patient_appointment in patient_appointments:
            slot_ids.append(patient_appointment['slot_id_id'])
        return slot_ids

    def update_appointment(self, target_slot_id, appointment_id):
        try:
            target_appointment = Appointments.objects.get(appointment_id= appointment_id)
            target_appointment.slot = target_slot_id
            target_appointment.save()
            return True
        except Appointments.DoesNotExist:
                return False

    def delete_appointment_by_appointment_id(self, app_id):
        appointment = Appointments.objects.get(appointment_id = app_id)
        appointments_serializer = AppointmentsSerializer(appointment)
        slot_id_of_appointment = appointments_serializer.data['slot_id']
        appointment.delete()
        return slot_id_of_appointment