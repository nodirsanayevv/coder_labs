from django.contrib import admin
from .models import Category, Contact, Service, User
# Register your models here.
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(User)
