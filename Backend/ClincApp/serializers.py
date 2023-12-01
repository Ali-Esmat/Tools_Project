from django.forms import ValidationError
from rest_framework import serializers
from ClincApp.models import Users, DoctorSlots, Appointments
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(user_name=clean_data['user_name'], password=clean_data['password'])
		user_obj.user_type = clean_data['user_type']
		user_obj.save()
		return user_obj

class UserLoginSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(user_name=clean_data['user_name'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')

        user = Users.objects.get(user_name__exact=user.user_name)
        return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('user_name', 'user_type')

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