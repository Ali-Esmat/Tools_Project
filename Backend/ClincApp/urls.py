from os import path
from django.urls import re_path, path
from ClincApp.views import user_view
from ClincApp.views import appointment_view
from ClincApp.views import doctor_slots_view
from ClincApp.views.auth_views import UserRegisterView, UserLogin, UserLogout, UserView


urlpatterns=[
    re_path(r'^user/$', user_view.UserApi, name='user_no_param_url'),
    re_path(r'^user/(?P<user_id>\d+)/$', user_view.UserWithParamterApi, name='user_param_url'),
    re_path(r'^doctor/$', user_view.DoctorApi, name='doctor_no_param_url'),
    re_path(r'^patient/(?P<user_name>\w+)/$', user_view.PatientApi, name='patient_no_param_url'),
    re_path(r'^doctor_slots/$', doctor_slots_view.DoctorSlotsApi, name='doctor_slots_no_param_url'),
    re_path(r'^doctor_slots/(?P<id>\d+)/$', doctor_slots_view.DoctorSlotsWithParamterApi, name='doctor_slots_param_url'),
    re_path(r'^doctor_slots/user_view/(?P<id>\d+)/$', doctor_slots_view.DoctorSlotsPatientViewWithParamterApi, name='doctor_slots_user_view_param_url'),
    re_path(r'^appointments/$', appointment_view.AppointmentApi, name='appointment_no_param_url'),
    re_path(r'^appointments/(?P<id>\d+)/$', appointment_view.AppointmentWithParamterApi, name='appointment_param_url'),
	path('register', UserRegisterView.as_view(), name='register'),
	path('login', UserLogin.as_view(), name='login'),
	path('logout', UserLogout.as_view(), name='logout'),
	path('user', UserView.as_view(), name='user'),
]

# http://127.0.0.1:8000/api-token-auth/ -> obtain the auth token
# http://127.0.0.1:8000/api/get-details -> view current logged in user details
# http://127.0.0.1:8000/api/register -> add a new user