class User():
    def __init__(self, id, name):
        self.public_id = id
        self._name = name
        self._access_level = "user"

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._access_level = "admin"

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"User {user.get_name()} has been successfully added to the list")

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"User {user.get_name()} has been successfully removed from the list")

users = []
user1 = User("2345", "Andy Warhall")
admin = Admin("5656", "John Snow")

print(admin.public_id)
print(admin._name)
print(admin.get_access_level())

print(user1.get_name())
admin.add_user(users, user1)

