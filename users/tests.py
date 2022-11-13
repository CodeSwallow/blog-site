from django.test import TestCase

from users.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="user_1", password="password_123")

    def test_object_name_is_last_name_comma_first_name(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.last_name}, {user.first_name}'
        self.assertEqual(str(user), expected_object_name)
