from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()

def custom_validation(data):
    user_name = data['user_name'].strip()
    password = data['password'].strip()
    ##
    if not user_name or UserModel.objects.filter(user_name=user_name).exists():
        raise ValidationError('choose another email')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not user_name:
        raise ValidationError('choose another username')
    return data


def validate_user_name(data):
    user_name = data['user_name'].strip()
    if not user_name:
        raise ValidationError('choos another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True