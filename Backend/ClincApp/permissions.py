from rest_framework import permissions

class PatientPermission(permissions.BasePermission):

    message = "not a patient."

    def has_permission(self, request, view):
        if request.user.user_type == 'patient':
            return  True
        return False

class DoctorPermission(permissions.BasePermission):

    message = "not a doctor"
    def has_permission(self, request, view):
        if request.user.user_type == 'doctor':
            return  True
        return False