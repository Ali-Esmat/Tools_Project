from datetime import datetime, timedelta
from ClincApp.models import DoctorSlots
from ClincApp.serializers import DoctorSlotsSerializer
class DoctorSlotsRepository:
    def create_doctor_slot(self, slot_data):
        doctor_slot_serializer = DoctorSlotsSerializer(data= slot_data)
        if doctor_slot_serializer.is_valid():
            doctor_slot_serializer.save()
            return True
        else:
            return False

    def get_all_slots_for_a_doctor(self,doctor_id):
        slots_qs = DoctorSlots.objects.filter(doctor_id = doctor_id)
        slots = list(slots_qs.values())
        return slots

    def get_all_slots(self):
        slots = DoctorSlots.objects.all()
        slots_serializer = DoctorSlotsSerializer(slots, many=True)
        return slots_serializer

    def does_slot_collide(self, slot_date, slot_before_start_time_check, slot_end_time, doctor_id):
        try:
            slots_qs = DoctorSlots.objects.filter(date__exact = slot_date, start_hour__range = (slot_before_start_time_check, slot_end_time), doctor_id__exact = doctor_id)
            slots = list(slots_qs.values())
        except DoctorSlots.DoesNotExist:
             slots = []
        if  slots != []:
            return True
        else:
            return False

    def does_slot_collide_Update(self, slot_date, slot_before_start_time_check, slot_end_time, doctor_id, slot_id):
        try:
            slots_qs = DoctorSlots.objects.filter(date__exact = slot_date, start_hour__range = (slot_before_start_time_check, slot_end_time), doctor_id__exact = doctor_id)
            slots = list(slots_qs.values())
            i = 0
            while i < len(slots):
                if slots[i]['slot_id'] == int(slot_id):
                    slots.pop(i)
                i += 1
        except DoctorSlots.DoesNotExist:
             slots = []
        if  slots != []:
            return True
        else:
            return False

    def delete_a_slot_by_slot_id(self, id):
        slot = DoctorSlots.objects.get(slot_id=id)
        slot.delete()

    def update_slot_details_by_slot_id(self, slot_data, id):
        slot = DoctorSlots.objects.get(slot_id = id)
        slot_serializer = DoctorSlotsSerializer(slot, data=slot_data)
        if slot_serializer.is_valid():
            slot_serializer.save()
            return True
        else:
            return False

    def get_a_slot_by_slot_id(self,id):
        slot = DoctorSlots.objects.get(slot_id__exact = id)
        slot_serializer = DoctorSlotsSerializer(slot, many = False)
        return slot_serializer

    def get_a_slot_object_by_slot_id_(self,id):
        slot = DoctorSlots.objects.get(slot_id = id)
        print ("Doctor_slots_object : {}".format(slot))
        return slot

    def update_slot_status(self, status,slot_id):
        try:
            slot = DoctorSlots.objects.get(slot_id = slot_id)
            slot.status = status
            slot.save()
            return True
        except DoctorSlots.DoesNotExist:
            return False

    # utility
    def get_slot_id_by_date_and_time_and_doctor_id(self, slot_date, slot_time, doctor_id):
        print("slot_date : {}, start_hour : {}, doctor_id : {} ".format(slot_date,slot_time,doctor_id))
        slot_qs = DoctorSlots.objects.filter(date__exact = slot_date, start_hour__exact = slot_time, doctor_id__exact = doctor_id).values_list('slot_id', flat=True)
        return slot_qs[0]

    def get_all_slots_of_a_doctor(self, doctor_id):
        slot_qs = DoctorSlots.objects.filter(doctor_id__exact = doctor_id).values_list('slot_id','date','doctor','start_hour','status').order_by('date', 'start_hour')
        return list(slot_qs)

    def get_all_slots_of_a_doctor_Patient_view(self, doctor_id):
        print("here")
        slot_qs = DoctorSlots.objects.filter(doctor_id__exact = doctor_id, status__exact = "AVALIABLE").values_list('slot_id','date','doctor','start_hour').order_by('date', 'start_hour')
        return list(slot_qs)