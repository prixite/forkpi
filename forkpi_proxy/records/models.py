from django.db import models


class User(models.Model):
    class Meta:
        managed = False
        db_table = "auth_user"

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)


class Profile(models.Model):
    class Meta:
        managed = False

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, default="", null=True, blank=True)


class Keypair(models.Model):
    class Meta:
        managed = False

    name = models.TextField(null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, default="", null=True, blank=True)
    is_active = models.BooleanField(default=True)


class AppConfig(models.Model):
    global_pin = models.TextField(default="", db_index=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "reocords_appconfig"
