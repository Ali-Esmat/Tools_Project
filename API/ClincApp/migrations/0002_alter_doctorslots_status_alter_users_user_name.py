# Generated by Django 4.2.7 on 2023-11-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClincApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorslots',
            name='status',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
