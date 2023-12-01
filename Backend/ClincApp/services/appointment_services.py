from ClincApp.repo.appointments_repository import AppointmentsRepository
from ClincApp.serializers import AppointmentsSerializer
from ClincApp.services import slot_services
from ClincApp.services import user_services

# Get all Appointments in the database
def get_all_appointments():
    appointments_repository = AppointmentsRepository()
    appointment_serializer = AppointmentsRepository.get_all_appointments(appointments_repository)
    response = list(appointment_serializer.data)
    return response
# Get all the appointments related to a specific patient from the database
def get_all_appointments_for_patient(patient_id):
    appointments_repository = AppointmentsRepository()
    response = AppointmentsRepository.get_appointment_by_patient_id(appointments_repository, patient_id)
    return response

    '''appointments_list = list(appointments_serializer.data)
    appointment_details_list = []
    for i, appointment in enumerate(appointments_list):
        slot_id = appointment[i]['slot']
        appointment_details_list += slot_services.get_appointment_details(slot_id)
    return response '''


# POST a new appointment into the database
# takes the slot id and the user id in the request data
# uses slot id to check if the slot is reserved first
# then checks for collison, types of collison:
# 1. the user with the current user id already has an appointment with this slot
# 2. the user with the current user id has an appointment with a different slot id but with the same date and time
#   2.1- get the user's appointments containing the slot ids using the patient id
#   2.2- get the slots related to those appointments using the slot ids (user related slots)
#   2.3- filter theses slots to keep only the slots with the same date and time
#   2.4 if any remains then collison = true
'''def create_appointment(slot_id, patient_id):
    if (slot_services.check_is_reserved(slot_id)):
        return False
    else:
        slot = slot_services.get_a_slot_object_by_slot_id_(slot_id)
        patient = user_services.get_user_by_id(patient_id)
        if check_for_appointment_collison(slot_id, patient_id):
            return False
        else:
            appointment_repository = AppointmentsRepository()
            if appointment_repository.create_appointment(slot_id, patient_id):
                if slot_services.update_slot_status("RESERVED", slot_id):
                    return True
                else:
                    print("Flow Series: part 10.1 @ appointment_service.create_appointment(), creation failed due to slot status update failure")
                    return False
            else:
                print("Flow Series: part 10.2 @ appointment_service.create_appointment(), creation failed due to appointment creation failure")
                return False '''

def create_appointment(request_data):
    slot_id = request_data['slot_id']
    patient_id = request_data['patient_id']
    if (slot_services.check_is_reserved(slot_id)):
        return False
    else:
        #slot = slot_services.get_a_slot_object_by_slot_id_(slot_id)
        #patient = user_services.get_user_by_id(patient_id)
        if check_for_appointment_collison(slot_id, patient_id):
            return False
        else:
            appointment_repository = AppointmentsRepository()
            if appointment_repository.create_appointment(request_data):
                if slot_services.update_slot_status("RESERVED", slot_id):
                    return True
                else:
                    print("Flow Series: part 10.1 @ appointment_service.create_appointment(), creation failed due to slot status update failure")
                    return False
            else:
                print("Flow Series: part 10.2 @ appointment_service.create_appointment(), creation failed due to appointment creation failure")
                return False

def check_for_appointment_collison(slot_to_be_reserved_id, patient_id):
    # get the slot to be reserved using the slot_id (responsiblitiy of slot services)
    # get a list of slot ids related to the patient id (responsibility of appointment service)
    # iterate on the slot ids list and each time check if date and time of that slot causes a collsion with the slot to be reserved (responsibility of slot services)
    appointments_repository = AppointmentsRepository()
    patient_reserved_slot_ids = appointments_repository.get_patient_reserved_slot_ids(patient_id)
    for patient_reserved_slot_id in patient_reserved_slot_ids:
        if slot_services.check_patient_level_collsion(slot_to_be_reserved_id, patient_reserved_slot_id):
            return True
    return False

# we need to not match the alredy existing, reserved slot

def check_for_appointment_update_collison(target_slot_id, patient_id, slot_id_to_be_ignored):
    appointments_repository = AppointmentsRepository()
    patient_reserved_slot_ids = appointments_repository.get_patient_reserved_slot_ids(patient_id)
    print("Slot id to be ignored, this value should be 7 : {}".format(slot_id_to_be_ignored))
    for patient_reserved_slot_id in patient_reserved_slot_ids:
        if patient_reserved_slot_id != slot_id_to_be_ignored:
            if slot_services.check_patient_level_collsion(target_slot_id, patient_reserved_slot_id):
                print("the slot that caused the collison has the id: {}".format(patient_reserved_slot_id))
                return True
    return False

 # Update an appointment by choosing a slot with a different slot id
def update_appointment_by_slot_id(request_data, appointment_id):
# need to check if the slot is reserved by some else
# need to check if the slot collides with other users
    target_slot_id = request_data['slot_id']
    patient_id = request_data['patient_id']
    if slot_services.check_is_reserved(target_slot_id):
        print("Slot is reserved")
        return False
    else:# checks if the new slot is colliding with any other slots reserved by the patient
        appointment_repository = AppointmentsRepository()
        appointment_to_be_changed = appointment_repository.get_appointment_by_appointment_id(appointment_id)
        appointment_serializer = AppointmentsSerializer(appointment_to_be_changed, many = False)
        slot_id_to_be_ignored = appointment_serializer.data['slot_id']
        if check_for_appointment_update_collison(target_slot_id, patient_id, slot_id_to_be_ignored):
            print("Slot caused a collison")
            return False
        else:
            if appointment_repository.update_appointment(target_slot_id, appointment_id):
                return True
            else:
                print ("Slot failed to be updated")
                return False


# Delete an appointment by appointment id
def delete_appointment_by_appointment_id(appointment_id):
    appointment_repository = AppointmentsRepository()
    slot_id_of_appointment = appointment_repository.delete_appointment_by_appointment_id(appointment_id)
    if slot_services.update_slot_status('AVALIABLE', slot_id_of_appointment):
        return True
    else:
        return False


# Get all the doctor names in the database
def get_all_doctor_names():
    return user_services.get_all_doctor_names()

def get_all_slots_of_a_doctor_by_name(doctor_name):
    return slot_services.get_all_slots_of_a_doctor_by_name(doctor_name)

def Make_appointment_using_slot_details(request_data):
    date = request_data['date']
    start_hour = request_data['start_hour']
    doctor_name = request_data['doctor_name']
    patient_name = request_data['patient_name']
    patient_id = user_services.get_user_id_by_name(patient_name)
    slot_id = slot_services.get_slot_id_by_date_and_time_and_doctor_name(date,start_hour,doctor_name)
    if create_appointment(slot_id, patient_id):
        return True
    else:
        return False
