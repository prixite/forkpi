from django.test import TestCase
from records.models import AppConfig, User, Door
from spoonpi.spoonpi.forkpi_db import ForkpiDB


class ForkpiDBTestCase(TestCase):
    def setUp(self):
        AppConfig.objects.get_or_update_global_pin("1234")
        Door.objects.create(name="Test Door", serial="0000000000000000")
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.db = ForkpiDB()

    def test_global_pin_authentication(self):
        is_authorized, names = self.db.authenticate(
            global_pin="1234", username="testuser"
        )
        self.assertTrue(is_authorized)
        self.assertEqual(names, [self.user])
