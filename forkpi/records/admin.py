from django.contrib import admin
from records import models

admin.site.register(models.Keypair)
admin.site.register(models.Profile)
admin.site.register(models.AppConfig)