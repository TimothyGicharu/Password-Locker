import unittest
from login import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.new_credentials = Credentials("Twitter","TGicharu","index506119056")

    def tearDown(self):
        """
        Tear down method to run before each teat case
        """
        Credentials.credentials_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.account_name, "Twitter")
        self.assertEqual(self.new_credentials.user_name, "TGicharu")
        self.assertEqual(self.new_credentials.password, "index506119056")

    def test_save_credentials(self):
        """
        test_save_credentials test case to check if the credentials are saved
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our contact_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Facebook","TMunene","123456789")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_display_credentials(self):
        """
        test_display_credentials test case to test if the credentials are
        displayed upon request
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_delete_credentials(self):
        """
        test_delete_credential test case to check if a user can delete credentials
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Facebook","TMunene","123456789")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credential_by_account_name(self):
        '''
        test to check if we can find the credentials of an account and display
         to the user upon request
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","TMunene","123456789")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account_name("Facebook")

        self.assertEqual(found_credentials.account_name, test_credentials.account_name)

if __name__ == "__main__":
    unittest.main()
