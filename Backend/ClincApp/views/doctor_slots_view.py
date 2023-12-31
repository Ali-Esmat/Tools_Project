from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ClincApp.services import slot_services
from ClincApp.permissions import DoctorPermission, PatientPermission

@csrf_exempt
def DoctorSlotsApi(request):
    # request format: api/doctor_slots
    # request format: api/doctor_slots/
    # Get all slots in the database
    permission_classes = (IsAuthenticated, DoctorPermission|PatientPermission)
    if request.method == 'GET':
        response = slot_services.get_all_slots()
        return JsonResponse(response,safe=False)
    # request format: api/doctor_slots
    # request format: api/doctor_slots/
    # POST a new slot into the database
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        if slot_services.create_doctor_slot(request_data):
            #return Response(status=status.HTTP_201_CREATED)
            return JsonResponse("Added successfully", status=status.HTTP_201_CREATED, safe=False)
        else:
            #return Response(status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse("Failed to add the slot", status=status.HTTP_400_BAD_REQUEST, safe=False)

@csrf_exempt
def DoctorSlotsWithParamterApi(request, id):

    permission_classes = (IsAuthenticated, DoctorPermission)
    # request format: api/doctor_slots/<id>/
    # Get all the slots related to a specific doctor from the database
    if request.method == 'GET':
        doctor_id = id
        response = slot_services.get_all_slots_for_a_doctor(doctor_id)
        return JsonResponse(response,safe=False)

    # request format: api/doctor_slots/<id>/
    # Update a slot by slot id
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        slot_id = id
        if slot_services.update_slot_details_by_slot_id(request_data, slot_id):
            return JsonResponse("Updated the slot successfully", safe=False)
        else:
            return JsonResponse("Failed to update the slot", safe=False)
    # request format: api/doctor_slots/<id>/
    # Delete a slot by slot id
    elif request.method == 'DELETE':
        if slot_services.delete_a_slot_by_slot_id(id):
            return JsonResponse("Deleted the slot successfully", safe=False)
        else:
            return JsonResponse("Failed to delete the slot, it does not exist", safe= False)

@csrf_exempt
def DoctorSlotsPatientViewWithParamterApi(request, id):
        if request.method == 'GET':
            doctor_id = id
            response = slot_services.get_all_slots_for_a_doctor_Patient_view(doctor_id)
            return JsonResponse(response,safe=False)