from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from ClincApp.permissions import PatientPermission
from ClincApp.services import appointment_services

@csrf_exempt
def AppointmentApi(request):
    # request format: api/appointments
    # request format: api/appointments/
    # Get all Appointments in the database
    if request.method == 'GET':
        response = appointment_services.get_all_appointments()
        return JsonResponse(response,safe=False)
    # request format: api/appointments
    # request format: api/appointments/
    # POST a new appointment into the database
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        print(request_data)
        if appointment_services.create_appointment(request_data):
            return JsonResponse("Appointment added successfully", safe=False)
        else:
            return JsonResponse("Failed to add the appointment", safe=False)

@csrf_exempt
def AppointmentWithParamterApi(request, id):

    permission_classes = (IsAuthenticated, PatientPermission)
    # request format: api/appointments/<id>/
    # Get all the appointments related to a specific patient from the database
    if request.method == 'GET':
        patient_id = id
        response = appointment_services.get_all_appointments_for_patient(patient_id)
        return JsonResponse(response,safe=False)
    # request format: api/appointments/<id>/
    # Update an appointment by choosing a slot with a different slot id
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        appointment_id = id
        if appointment_services.update_appointment_by_slot_id(request_data, appointment_id):
            return JsonResponse("Updated the slot in the appointment successfully", safe=False)
        else:
            return JsonResponse("Failed to update the slot in the appointment", safe=False)
    # request format: api/appointments/<id>/
    # Delete an appointment by appointment id
    elif request.method == 'DELETE':
        if appointment_services.delete_appointment_by_appointment_id(id):
            return JsonResponse("Deleted the appointment successfully", safe=False)
        else:
            return JsonResponse("Failed to delete the appointment", safe=False)