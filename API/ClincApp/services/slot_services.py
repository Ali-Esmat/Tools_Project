from datetime import datetime, timedelta
from ClincApp.repo.doctor_slots_repository import DoctorSlotsRepository


# utility functions
def check_update_collison(request_data, slot_id):
    slot_date = request_data['date']
    slot_time = request_data['start_hour']
    parsed = parse_time(slot_date, slot_time)
    if len(slot_date) == 0 | len(slot_time) == 0:
        return False
    doctor_slots_repository = DoctorSlotsRepository()
    if doctor_slots_repository.does_slot_collide_Update(slot_date, parsed[0], parsed[1], slot_id):
        return True
    else:
        return False

def parse_time(slot_date, slot_time):
    date_format = '%Y-%m-%d %H:%M'
    slot_start_time = datetime.strptime(slot_date + " " + slot_time, date_format)
    slot_end_time = slot_start_time + timedelta(minutes=59)
    slot_before_start_time_check = slot_start_time - timedelta(minutes=59)
    output = [slot_before_start_time_check, slot_end_time]
    return output

def check_time_collison(request_data):
    slot_date = request_data['date']
    slot_time = request_data['start_hour']
    parsed = parse_time(slot_date, slot_time)
    if len(slot_date) == 0 | len(slot_time) == 0:
        return False
    doctor_slots_repository = DoctorSlotsRepository()
    if doctor_slots_repository.does_slot_collide(slot_date, parsed[0], parsed[1]):
        return True
    else:
        return False

# Get all slots in the database
def get_all_slots():
    doctor_slots_repository = DoctorSlotsRepository()
    slots_serializer = DoctorSlotsRepository.get_all_slots(doctor_slots_repository)
    response = list(slots_serializer.data)
    return response

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
    slots = doctor_slots_repository.get_all_slots_for_a_doctor(doctor_id)
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
 # Delete a slot by slot id
def delete_a_slot_by_slot_id(slot_id):
    doctor_slots_repository = DoctorSlotsRepository()
    doctor_slots_repository.delete_a_slot_by_slot_id(slot_id)