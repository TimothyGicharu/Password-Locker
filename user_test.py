import unittest
from login import User

class TestUser(unittest.TestCase):
    """
    Test case that defines test cases for the user class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_user = User("Timothy", "index506119056")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.users_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name,"Timothy")
        self.assertEqual(self.new_user.user_password,"index506119056")

    def test_save_user(self):
        """
        test_save_user test case to see if the user object is saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def test_add_multiple_users(self):
        """
        test_add_user test case that tests to see if a user is added
        """
        self.new_user.save_user()
        test_user = User("TestUser", "123456789")
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)

    def test_delete_user(self):
        """
        test_delete_user test case to test if we can delete a user from the
        users_list
        """
        self.new_user.save_user()
        test_user = User("TestUser", "123456789")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.users_list),1)

    def test_display_users(self):
        """
        test_display_user test case to check if all users can be displayed
        upon request
        """
        self.assertEqual(User.display_users(),User.users_list)


if __name__ == '__main__':
    unittest.main()
