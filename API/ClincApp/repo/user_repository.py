import itertools
from ClincApp.models import Users
from ClincApp.serializers import UsersSerializer
class UserRepository:
    # (self, user_name, password, user_type)
    def create_user(self, user_data):
        users_serializer = UsersSerializer(data= user_data)
        if users_serializer.is_valid():
            print("User serialized data: {}".format(users_serializer.validated_data))
            users_serializer.save()
            return True
        else:
            return False

    def get_all(self):
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        print("user serializer : {}".format(users_serializer))
        print("user serializer data: {}".format(users_serializer.data))
        return users_serializer

    def get_user(self,id):
        #user_serializer = UsersSerializer(Users.objects.get(user_id =id), many = False)
        user = Users.objects.get(user_id =id)
        return user

    def delete_user(self, id):
        user = Users.objects.get(user_id=id)
        user.delete()

    def update_user(self, user_data, id):
        user = Users.objects.get(user_id = id)
        users_serializer = UsersSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return True
        else:
            return False

    # None path functions
    def get_user_id_by_name(self, user_name):
        #user_qs = Users.objects.filter(user_name = user_name).values_list('user_id', flat= True)
        #return user_qs[0]
        try:
            user = Users.objects.get(user_name__exact = user_name)
            user_serializer = UsersSerializer(user, many = False)
            return user_serializer.data
        except Users.DoesNotExist:
            return []


    def get_user_name_by_id(self, user_id):
        user_qs = Users.objects.filter(user_id = user_id).values_list('user_name', flat= True)
        return user_qs[0]

    def get_all_patients(self):
        users_qs = Users.objects.filter(user_type= "patient").values_list('user_name', flat=True)
        return list(users_qs)

    def get_all_doctors(self):
        doctors_qs = Users.objects.filter(user_type= "doctor").values_list('user_id','user_name')
        #doctors = list(itertools.chain(*doctors_qs))
        #doctors = UsersSerializer(doctors_qs, many = True)
        return list(doctors_qs)
        '''
        filter("object filter attribute").
        values('files_id') -> returns a specific attribute as a list of dicitonaries
        values_list('files_id', flat=True).order_by('id') -> returns a specific attribute as a list of values ordered on a specific attribute

        '''
        #return user['user_id']
