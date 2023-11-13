from rest_framework import serializers
from ClincApp.models import Users, DoctorSlots, Appointments

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=("user_id","user_name","password","user_role")

class DoctorSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorSlots
        fields=("slot_id","date","start_hour","doctor","status")

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointments
        fields=("appointment_id","slot_id","patient_id")

class CreateAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointments
        fields=("slot_id","patient_id")