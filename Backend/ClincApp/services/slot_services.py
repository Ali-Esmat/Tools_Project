from datetime import datetime, timedelta
from ClincApp.repo.doctor_slots_repository import DoctorSlotsRepository
from ClincApp.serializers import DoctorSlotsSerializer
from ClincApp.services.user_services import get_user_id_by_name
#from ClincApp.response import AppointmentDetailsResponse
# utility functions
def check_update_collison(request_data, slot_id):
    slot_date = request_data['date']
    slot_time = request_data['start_hour']
    doctor_id = request_data['doctor']
    parsed = parse_time(slot_date, slot_time)
    # this check might be useless
    if len(slot_date) == 0 | len(slot_time) == 0:
        return False
    doctor_slots_repository = DoctorSlotsRepository()
    if doctor_slots_repository.does_slot_collide_Update(slot_date, parsed[0], parsed[1], doctor_id, slot_id):
        return True
    else:
        return False

def parse_time(slot_date, slot_time):
    slot_start_time = get_date_time_obj_format(slot_date, slot_time)
    slot_end_time = slot_start_time + timedelta(minutes=59)
    slot_before_start_time_check = slot_start_time - timedelta(minutes=59)
    output = [slot_before_start_time_check, slot_end_time]
    return output

def get_date_time_obj_format(slot_date, slot_time):
    date_format = "%Y-%m-%d %H:%M:%S"
    return datetime.strptime(slot_date + " " + slot_time, date_format)

def check_time_collison(request_data):
    slot_date = request_data['date']
    slot_time = request_data['start_hour']
    doctor_id = request_data['doctor']
    parsed = parse_time(slot_date, slot_time)
    if len(slot_date) == 0 | len(slot_time) == 0:
        return False
    doctor_slots_repository = DoctorSlotsRepository()
    if doctor_slots_repository.does_slot_collide(slot_date, parsed[0], parsed[1], doctor_id):
        return True
    else:
        return False
    '''
    - the doctor can not create a slot that collides with a slot that is already taken by him
    - two doctors can have colliding slots
    '''
def check_is_reserved(slot_id):
    doctor_slots_repository = DoctorSlotsRepository()
    slot_serialzier = doctor_slots_repository.get_a_slot_by_slot_id(slot_id)
    if (slot_serialzier.data['status'] == 'RESERVED'):
        return True
    else:
        return False

def check_patient_level_collsion(slot_to_be_reserved_id, patient_reserved_slot_id):
    slot_to_be_reserved_collsion_range =  get_a_slot_collsion_range(slot_to_be_reserved_id)
    already_reserved_slot_serializer = get_a_slot_by_id(patient_reserved_slot_id)
    # do the serializer types need to be casted ?
    already_reserved_slot_start_time = get_date_time_obj_format(already_reserved_slot_serializer.data['date'],already_reserved_slot_serializer.data['start_hour'])
    if slot_to_be_reserved_collsion_range[0] <= already_reserved_slot_start_time <=slot_to_be_reserved_collsion_range[1]:
        # time collison occurs
        return True
    else:
        return False


def get_a_slot_collsion_range(slot_id):
    slot_serializer = get_a_slot_by_id(slot_id)
    slot_date = slot_serializer.data['date']
    slot_time = slot_serializer.data['start_hour']
    slot_collsion_range = parse_time(slot_date, slot_time)
    return slot_collsion_range

# Get all slots in the database
def get_all_slots():
    doctor_slots_repository = DoctorSlotsRepository()
    slots_serializer = DoctorSlotsRepository.get_all_slots(doctor_slots_repository)
    response = list(slots_serializer.data)
    return response

# Get a slot by id
def get_a_slot_by_id(slot_id):
    doctor_slots_repository = DoctorSlotsRepository()
    slot = DoctorSlotsRepository.get_a_slot_by_slot_id(doctor_slots_repository, slot_id)
    #response = list(slots_serializer.data)
    #eturn response
    return slot

def get_a_slot_object_by_slot_id_(slot_id):
    doctor_slots_repository = DoctorSlotsRepository()
    slot = DoctorSlotsRepository.get_a_slot_object_by_slot_id_(doctor_slots_repository, slot_id)
    slot_serializer = DoctorSlotsSerializer(slot, many = False)
    print ("Doctor_slots_serializer_object : {}".format(slot_serializer.data))
    return slot_serializer.data

# POST a new slot into the database
def create_doctor_slot(request_data):
        if check_time_collison(request_data):
            return False
        doctor_slots_repository = DoctorSlotsRepository()
        if doctor_slots_repository.create_doctor_slot(request_data):
            return True
        else:
            return False

# Get all the slots related to a specific doctor from the database
def get_all_slots_for_a_doctor(doctor_id):
    doctor_slots_repository = DoctorSlotsRepository()
    slots = doctor_slots_repository.get_all_slots_of_a_doctor(doctor_id)
    return slots

def get_all_slots_for_a_doctor_Patient_view(doctor_id):
    doctor_slots_repository = DoctorSlotsRepository()
    slots = doctor_slots_repository.get_all_slots_of_a_doctor_Patient_view(doctor_id)
    return slots

# Update a slot by slot id
def update_slot_details_by_slot_id(request_data, slot_id):
    if check_update_collison(request_data, slot_id):
            return False
    doctor_slots_repository = DoctorSlotsRepository()
    if doctor_slots_repository.update_slot_details_by_slot_id(request_data, slot_id):
        return True
    else:
        return False

def update_slot_status(status, slot_id):
    doctor_slots_repository = DoctorSlotsRepository()
    if doctor_slots_repository.update_slot_status(status, slot_id):
        return True
    else:
        return False
 # Delete a slot by slot id
def delete_a_slot_by_slot_id(slot_id):
    doctor_slots_repository = DoctorSlotsRepository()
    return doctor_slots_repository.delete_a_slot_by_slot_id(slot_id)


# non path related functions
def get_slot_id_by_date_and_time_and_doctor_name(slot_date, slot_time, doctor_name):
    doctor_slots_repository = DoctorSlotsRepository()
    doctor_id = get_user_id_by_name(doctor_name)
    slot_id = doctor_slots_repository.get_slot_id_by_date_and_time_and_doctor_id(slot_date, slot_time, doctor_id)
    return slot_id

def get_all_slots_of_a_doctor_by_name(doctor_name):
    doctor_id = get_user_id_by_name(doctor_name)
    doctor_slots_repository = DoctorSlotsRepository()
    slots_details_list = doctor_slots_repository.get_all_slots_of_a_doctor(doctor_id)
    return slots_details_list