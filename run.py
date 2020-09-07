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

# def delete_user(user):
#     """
#     Function to delete a user
#     """
#     user.delete_user()

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

def find_credentials(account_name):
    '''
    Function that finds a credential by number and returns the credential
    '''
    return Credentials.find_by_account_name(account_name)

def display_credentials():
    """
    Function to display all credentials
    """
    return Credentials.display_credentials()

# Calling our Functions

def main():
    print("Hello. Welcome to Password Locker. Create username...")
    user_name = input()
    print("Create password...")
    user_password = input()

    save_user(create_user(user_name, user_password))
    print("\n")
    print("{}, kindly input your password to login...".format(user_name))
    enter_password = input()

    if enter_password == user_password:
        print("\n Logged in!")

        while True:
            print("~"*16)
            print("What would you like to do?")
            print("\n")
            print("Use these short codes : cu - Create Username and password, dc - Display Credentials, sc - Search for credentials account, du - Delete Credentials, ex - Exit password locker")
            # sc - Save Credentials, sc - Show / Display Credentials, dc - Delete credentials, ex - Exit User Account
            short_code = input().lower()

            if short_code == "cu":
                print("~" * 15)
                print("Enter account name.....")
                account_name= input()
                print("Enter username ...")
                user_name = input()
                print("~" * 15)
                print("Create password")
                password = input()
                
                save_credentials(create_credentials(account_name,user_name,password))
                print("\n")
                print("Account added")
                print("Account: {account_name} User name: {user_name} Password: {password}")
                print("\n")

            elif short_code == "dc":
                if display_credentials():
                    print("Your accounts:")
                    print("\n")

                    for credentials in display_credentials():
                        print("Account: {credentials.account_name} / Username: {credentials.user_name} / Password: {password}")
                    print("\n")
                else:
                    print("No accounts saved.")
                    print("\n")

            elif short_code == "sc":
                print("Enter the account you want to find...")
                account = input()

                if find_credentials(account):
                    account = find_credentials(account)
                    print("{account.user_name} {account.password}")
                    print("\n")

                else:
                    print("That account does not exist")
                
            elif short_code == "du":
                print("Account to be deleted...")
                delete_account = input()

                if find_credentials(delete_account):
                    delete_credentials(find_credentials(delete_account))
                    print("~"*16)
                    print("Account deleted!")

            elif short_code == "ex":
                print("Have a nice day!")
                break

            else:
                print("Enter a valid short code!")

    else:
        print("Wrong password!")

if __name__ == '__main__':
    main()








            #     #create and save a new user
            #     save_user(create_user(user_name, password))
            #     print("\n")
            #     print("New user {} created.".format(user_name))

            # elif short_code == "lu":
            #     print("Enter user name.....")
            #     user_name = input()

            #     if user_name in User.users_list:
            #         print("Logged in!")
            #         print('\n')
            #     else:
            #         print("Failed")


            # elif short_code == "du":
            #     delete_account = input("Enter account name to be deleted...")
            #     print("Are you sure you want to delete this {} account?".format(delete_account))

            #     while True:
            #         delete_account.delete_user()
            #         break

            # else:
            #     print("Use the short codes provided!")


            # # elif short_code == "lu":
            # #     print("Enter user name .....")
            # #     user_name = input()
            # #     if user_name in User.users_list:
            # #         print("You are good to go")
            # #         print("Enter password.....")
            # #         password = input()
            # #         # if password ==
            # #     else:
            # #         print("User doesn't exist!")

            #     # print("\n")
            #     # print("Enter password .....")
            #     # password = input()
            #     # print("\n")
            #     #
            #     # for user in User.users_list:
            #     #     print(user)
            #     #     # if user_name ==


