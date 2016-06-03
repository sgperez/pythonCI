import unittest
from MyMessenger import MyMessenger

class MessageTestCase(unittest.TestCase):
    """Tests for `MyMessenger.py`."""

    def setUp(self):
        self.messenger_obj = MyMessenger()

    def tearDown(self):
        self.messenger_obj = None

    def test_message_is_empty(self):
        """Does get_message() is empty for a new instance?"""
        self.assertEqual(self.messenger_obj.get_message(),'')

    def test_assign_new_message(self):
        """ Can assign new message?"""
        my_message = 'hello'
        self.messenger_obj.new_message(my_message)
        self.assertEqual(self.messenger_obj.get_message(),my_message)


if __name__ == '__main__':
    unittest.main()
