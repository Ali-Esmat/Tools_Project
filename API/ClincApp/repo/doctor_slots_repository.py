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
        print(slots_serializer.data)
        return slots_serializer

    def does_slot_collide(self, slot_date, slot_before_start_time_check, slot_end_time):
        try:
            slots_qs = DoctorSlots.objects.filter(date__exact = slot_date, start_hour__range = (slot_before_start_time_check, slot_end_time))
            slots = list(slots_qs.values())

        except DoctorSlots.DoesNotExist:
             slots = []
        if  slots != []:
            return True
        else:
            return False

    def does_slot_collide_Update(self, slot_date, slot_before_start_time_check, slot_end_time, slot_id):
        try:
            slots_qs = DoctorSlots.objects.filter(date__exact = slot_date, start_hour__range = (slot_before_start_time_check, slot_end_time))
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
    # May not be required
    def get_a_slot_by_slot_id(self,id):
        slot = DoctorSlots.objects.get(slot_id = id)
        slot_serializer = DoctorSlotsSerializer(slot, many = False)
        return slot_serializer

    def update_slot_status(self, status,slot_id):
        slot = DoctorSlots.objects.get(slot_id = slot_id)
        slot_serializer = DoctorSlotsSerializer(slot)
        slot_serializer.data[0]['status'] = status
        if slot_serializer.is_valid():
            slot_serializer.save()
            return True
        else:
            return False