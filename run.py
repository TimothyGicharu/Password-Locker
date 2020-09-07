#!/usr/bin/env python3.7

from login import User
from login import Credentials

# User Functions
def create_user(user_name, user_password):
    """
    Function to create a new user
    """
    new_user = User(user_name, user_password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()

def delete_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

# Credentials Functions

def create_credentials(account_name,user_name,password):
    """
    Function to create user credentials
    """
    new_credentials = Credentials(account_name,user_name,password)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save credentials
    """
    credentials.save_credentials()

def delete_credentials(credentials):
    """
    Function to delete a credentials
    """
    credentials.delete_credentials()

def display_credentials():
    """
    Function to display all credentials
    """
    return Credentials.display_credentials()

# Calling our Functions

def main():
    print("Hello. Welcome to Paasword Locker. What shall we call you?")
    user_name = input()

    print("Hello {}. What would you like to do?".format(user_name))
    print("\n")

    while True:
        print("Use these short codes : cu - Create User, du - Delete User, lu - Login to Account")
        # sc - Save Credentials, sc - Show / Display Credentials, dc - Delete credentials, ex - Exit User Account
        short_code = input().lower()

        if short_code == "cu":
            print("Enter username")
            print("~" * 15)
            user_name= input()
            print("~" * 15)
            print("Enter password ...")
            password = input()

            #create and save a new user
            save_user(create_user(user_name, password))
            print("\n")
            print("New user {} created.".format(user_name))

        elif short_code == "lu":
            print("Enter user name.....")
            user_name = input()

            if user_name in User.users_list:
                print("Logged in!")
                print('\n')
            else:
                print("Failed")


        elif short_code == "du":
            delete_account = input("Enter account name to be deleted...")
            print("Are you sure you want to delete this {} account?".format(delete_account))

            while True:
                delete_account.delete_user()
                break

        else:
            print("Use the short codes provided!")


        # elif short_code == "lu":
        #     print("Enter user name .....")
        #     user_name = input()
        #     if user_name in User.users_list:
        #         print("You are good to go")
        #         print("Enter password.....")
        #         password = input()
        #         # if password ==
        #     else:
        #         print("User doesn't exist!")

            # print("\n")
            # print("Enter password .....")
            # password = input()
            # print("\n")
            #
            # for user in User.users_list:
            #     print(user)
            #     # if user_name ==

if __name__ == '__main__':
    main()
