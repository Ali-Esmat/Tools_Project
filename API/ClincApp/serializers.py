from rest_framework import serializers
from ClincApp.models import Users, DoctorSlots, Appointments
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  user_name = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=Users.objects.all())]
  )
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  user_type = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = Users
    fields = ('user_name', 'password', 'password2', 'user_type')

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = Users.objects.create(
      user_name=validated_data['user_name'],
      user_type=validated_data['user_type'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=("user_id","user_name","password","user_type")

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