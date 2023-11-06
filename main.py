print("Task 1:\n")

"""
Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
"email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
дані можна отримати лише через методи класу.
"""

# classes
class User:
    def __init__(self, name, age, email):
        self._name = name
        self.__age = age
        self.__email = email

    def print_user_info(self):
        print(f"Name: {self._name}\nAge: {self.__age}\nEmail: {self.__email}")

    # getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    # setters
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email



# objects
user1 = User("Alex", 25, "alex@gmail.com")
user3 = User("Brandon", 35, "brandon@gmail.com")
user4 = User("Ben", 45, "ben@gmail.com")


# main
print("User1 info:")
user1.print_user_info()

print("\nChanging User1 data:")
user1.set_name(input("Enter new name: "))
user1.set_age(input("Enter new age: "))
user1.set_email(input("Enter new email: "))

print("\nNew User1 info:")
user1.print_user_info()