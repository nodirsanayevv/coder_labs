from rest_framework import serializers
from .models import Contact, Category, Service, User

class ContactSerializer(serializers.ModelSerializer):

     class Meta:
         model = Contact
         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'