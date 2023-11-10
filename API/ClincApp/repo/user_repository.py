from ClincApp.models import Users
from ClincApp.serializers import UsersSerializer
class UserRepository:
    # (self, user_name, password, user_type)
    def create_user(self, user_data):
        users_serializer = UsersSerializer(data= user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return True
        else:
            print(users_serializer.errors)
            return False

    def get_all_patients(self):
        users = Users.objects.get(userType= "patient")
        users_serializer = UsersSerializer(users, many=True)
        return users_serializer

    def get_all(self):
        return Users.objects.all()

    def get_user(self,id):
        user_serializer = UsersSerializer(Users.objects.get(user_id =id), many = False)
        return user_serializer

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
