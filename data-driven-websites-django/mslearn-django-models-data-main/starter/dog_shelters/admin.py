from django.contrib import admin

from .models import Dog, Shelter

admin.site.register(Shelter)
admin.site.register(Dog)
