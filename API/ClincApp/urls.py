from django.urls import re_path
from ClincApp.api import user_view
from ClincApp.api import doctor_slots_view


urlpatterns=[
    re_path(r'^user/$', user_view.UserApi, name='user_no_param_url'),
    re_path(r'^user/(?P<user_id>\d+)/$', user_view.UserWithParamterApi, name='user_param_url'),
    re_path(r'^doctor_slots/$', doctor_slots_view.DoctorSlotsApi, name='doctor_slots_no_param_url'),
    re_path(r'^doctor_slots/(?P<id>\d+)/$', doctor_slots_view.DoctorSlotsWithParamterApi, name='doctor_slots_param_url')
]