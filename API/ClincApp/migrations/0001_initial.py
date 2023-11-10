# Generated by Django 4.2.7 on 2023-11-09 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('userType', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSlots',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_hour', models.TimeField()),
                ('status', models.CharField(choices=[('AVALIABLE', 'AVALIABLE'), ('RESERVED', 'RESERVED')], default='AVALIABLE', max_length=9)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClincApp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClincApp.users')),
                ('slot_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ClincApp.doctorslots')),
            ],
        ),
    ]
