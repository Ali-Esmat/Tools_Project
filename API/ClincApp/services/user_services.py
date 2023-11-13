from ClincApp.repo.user_repository import UserRepository
from ClincApp.serializers import UsersSerializer


# Path functions
# GET all users method
def get_all_users():
    user_repository = UserRepository()
    users_serializer = UserRepository.get_all(user_repository)
    response = list(users_serializer.data)
    return response
# POST creates a user
def create_user(request_data):
        user_repository = UserRepository()
        if user_repository.create_user(request_data):
              return True
        else:
              return False
# GET specific user by id
def get_user_by_id(user_id):
        user_repository = UserRepository()
        user = UserRepository.get_user(user_repository, user_id)
        users_serializer = UsersSerializer(user, many = False)
        return users_serializer.data

# PUT updates a specific user by id
def update_user(request_data, user_id):
      user_repository = UserRepository()
      if user_repository.update_user(request_data, user_id):
            return True
      else:
            return False

def delete_user(user_id):
      user_repository = UserRepository()
      user_repository.delete_user(user_id)

# None path functions
def get_user_id_by_name(user_name):
      user_repository = UserRepository()
      user_id = user_repository.get_user_id_by_name(user_name)
      return user_id

def get_user_name_by_id(user_id):
      user_repository = UserRepository()
      user_name = user_repository.get_user_name_by_id(user_id)
      return user_name

def get_all_patients_names():
      user_repository = UserRepository()
      patient_list_of_names = user_repository.get_all_patients()
      return patient_list_of_names

def get_all_doctors():
      user_repository = UserRepository()
      doctors = user_repository.get_all_doctors()
      return doctors
