class User:
    """
    Class that creates new users
    """
    users_list = []

    def __init__(self, user_name, user_password):
        """
        __init__ method that helps us define properties for our objects
        """

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        """
        save_user method to save user to the users_list
        """
        User.users_list.append(self)

    # def delete_user(self):
    #     """
    #     delete_user method to delete user from the users_list
    #     """
    #     User.users_list.remove(self)

    # @classmethod
    # def display_users(cls):
    #     """
    #     Method that returns the users_list
    #     """
    #     return cls.users_list


class Credentials:
    """
    Class that generates user credentials and stores them
    """
    credentials_list = []

    def __init__(self, account_name, user_name, password):
        """
        __init__ method that allows us to define propertied for our objects
        """

        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        """
        save_credentials method that allows us to save new credentials
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        method that deletes a specific credential from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credentials_list
        """
        return cls.credentials_list

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in account and returns a credential that matches that account.
        Args:
            account: account to search for
        Returns :
            Credential of person that matches the account.
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials 
