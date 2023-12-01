from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
	def create_user(self, user_name, password=None):
		if not user_name:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user_name = self.normalize_email(user_name)
		user = self.model(user_name=user_name)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, user_name, password=None):
		if not user_name:
			raise ValueError('A user name is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(user_name, password)
		user.is_superuser = True
		user.save()
		return user


class Users(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=500, default="", unique=True)
	user_type = models.CharField(max_length=500)
	USERNAME_FIELD = 'user_name'
	REQUIRED_FIELDS = ['user_type']
	objects = AppUserManager()
	def __str__(self):
		return self.user_name


class DoctorSlots(models.Model):
    slot_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_hour = models.TimeField()
    # doctors_id_cascade
    doctor = models.ForeignKey(Users, null= False, on_delete= models.CASCADE)
    status = models.CharField(max_length=500)

class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    # slots_id_cascade
    slot_id = models.OneToOneField('DoctorSlots', null=False, on_delete= models.CASCADE)
    # patients_id_cascade
    patient_id = models.ForeignKey(Users, null= False, on_delete= models.CASCADE)
