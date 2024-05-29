# We have three types of naming: PascalCase, camelCase and snake_case
# Name of Class: Using PascalCase


class User:  # this is class
    def __init__(self, user_id, user_name) -> None:
        print(f"New user with {user_name}/{user_id} being created ....")
        self.id = user_id  # this is attribute
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):  # this is method
        user.followers += 1
        self.following += 1


user_1 = User("002", "vinhhv")  # user_1 is object
user_2 = User("007", "heocon")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
