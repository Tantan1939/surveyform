from django.contrib import admin
from . models import *
from django.apps import apps


for each_model in apps.get_app_config('app').models.values():
    admin.site.register(each_model)
