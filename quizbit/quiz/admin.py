from django.contrib import admin
from .models import Users, Questions, History
# Register your models here.


# Registering the models in django administration for accessing the database
admin.site.register(Users)
admin.site.register(Questions)
admin.site.register(History)