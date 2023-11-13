from django.db import models

# Create your models here.

class Users(models.Model):

    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=500, unique=True)
    password = models.CharField(max_length=500)
    user_role = models.CharField(max_length=500)

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
