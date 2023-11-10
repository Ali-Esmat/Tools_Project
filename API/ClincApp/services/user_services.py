from ClincApp.repo.user_repository import UserRepository

# GET all users method
def get_all_users():
    user_repository = UserRepository()
    users_serializer = UserRepository.get_all(user_repository)
    response = list(users_serializer.values())
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
        users_serializer = UserRepository.get_user(user_repository, user_id)
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
