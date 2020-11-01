from django.contrib import admin
from .models import People
from .models import Address
from .models import Phone

# Register your models here.

admin.site.register(People)
admin.site.register(Address)
admin.site.register(Phone)
