from django.test import TestCase
from records.models import User, AppConfig
from spoonpi.spoonpi.forkpi_db import ForkpiDB


class ForkpiDBTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.db = ForkpiDB()

    def test_global_pin_authentication(self):
        app_config = AppConfig.objects.get_singleton()
        app_config.update_global_pin("1234")
        is_authorized, names = self.db.authenticate(
            global_pin="1234", username="testuser"
        )
        self.assertTrue(is_authorized)
        self.assertEqual(names, [self.user])
