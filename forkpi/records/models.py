from django.db.models import *
from django.contrib.auth.models import User

from datetime import datetime
from utils import GlobalPinMixin


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    phone_number = CharField(max_length=20, default="", null=True, blank=True)

    def __str__(self):
        return self.user.username


class Keypair(Model):
    name = TextField(null=False, blank=False, unique=True)
    is_active = BooleanField(default=True)

    doors = ManyToManyField("Door")
    phone_number = CharField(max_length=20, default="", null=True, blank=True)

    pin = TextField(default="", null=True, blank=True)
    rfid_uid = TextField(default="", null=True, blank=True)
    fingerprint_template = TextField(default="", null=True, blank=True)

    hash_pin = TextField(default="")
    hash_rfid = TextField(default="")

    last_edited_on = DateTimeField(
        default=datetime.now, auto_now=True, null=False, blank=False
    )
    # if user that edited is deleted, set last_edited_by to null (do not cascade delete)
    last_edited_by = ForeignKey(User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class Log(Model):
    created_on = DateTimeField(
        default=datetime.now, auto_now_add=True, null=False, blank=False
    )
    door = ForeignKey("Door")

    was_allowed = BooleanField(default=False)
    details = TextField(default="", null=True, blank=True)

    pin = TextField(default="", null=True, blank=True)
    rfid_uid = TextField(default="", null=True, blank=True)
    used_fingerprint = BooleanField(default=False)


class Option(Model):
    name = TextField(unique=True)
    value = TextField(default="")
    default = TextField()
    flavor_text = TextField(default="")
    description = TextField(default="")


class Door(Model):
    name = TextField(default="", unique=True)
    serial = TextField(unique=True)


class AppConfigManager(Manager, GlobalPinMixin):
    pass


class AppConfig(Model):
    global_pin = TextField(default="", null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    objects = AppConfigManager()
