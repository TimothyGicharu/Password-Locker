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


def create_credentials(account_name, user_name, password):
    """
    Function to create user credentials
    """
    new_credentials = Credentials(account_name, user_name, password)
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
            short_code = input().lower()

            if short_code == "cu":
                print("~" * 15)
                print("Enter account name.....")
                account_name = input()
                print("Enter username ...")
                user_name = input()
                print("~" * 15)
                print("Create password")
                password = input()

                save_credentials(create_credentials(account_name, user_name, password))
                print("\n")
                print("Account added")
                print(f"New account: {account_name} added \nUsername: {user_name} / Password:{password}")
                print("\n")

            elif short_code == "dc":
                if display_credentials():
                    print("Your accounts:")
                    print("\n")

                    for credentials in display_credentials():
                        print(credentials)
                        print(f"{credentials.account_name} {credentials.user_name} .....{credentials.password}")                 
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
