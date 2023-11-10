from django.urls import re_path
from ClincApp.api import user_view


urlpatterns=[
    re_path(r'^user/$', user_view.UserApi, name='user_no_param_url'),
    re_path(r'^user/(?P<user_id>\d+)/$', user_view.UserWithParamterApi, name='user_param_url')
]