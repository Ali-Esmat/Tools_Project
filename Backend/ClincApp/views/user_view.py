from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ClincApp.services import user_services
# Create your views here.

@csrf_exempt
def UserApi(request):
    # request format: api/user
    # request format: api/user/
    # GET all users in the database
    if request.method == 'GET':
        response = user_services.get_all_users()
        return JsonResponse(response,safe=False)
    # request format: api/user
    # request format: api/user/
    # POST a new user into the databases
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        if user_services.create_user(request_data):
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse("Failed to add user", safe=False)

@csrf_exempt
def UserWithParamterApi(request, user_id):
    # request format: api/user/<user_id>/
    # Get a user by id from the database
    if request.method == 'GET':
        response = user_services.get_user_by_id(user_id)
        return JsonResponse(response,safe=False)
    # request format: api/user/<user_id>/
    # Update a user by id
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        if user_services.update_user(request_data, user_id):
            return JsonResponse("Updated successfully", safe=False)
        else:
            return JsonResponse("Failed to updated", safe=False)
    # request format: api/user/<user_id>/
    # Delete a user by id
    elif request.method == 'DELETE':
        user_services.delete_user(user_id)
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def DoctorApi(request):
    # request format: api/doctor
    # request format: api/doctor/
    # GET all users in the database
    if request.method == 'GET':
        response = user_services.get_all_doctors()
        return JsonResponse(response,safe=False)
@csrf_exempt
def PatientApi(request, user_name):
    # request format: api/patient/<user_name>/
    # Get a user by name from the database
    if request.method == 'GET':
        response = user_services.get_user_id_by_name(user_name)
        return JsonResponse(response,safe=False)


# Get All users
# Create a user
# Get A user by ID
# Update a user by ID
# Delete a user by ID
