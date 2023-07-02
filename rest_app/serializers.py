from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentModel
#         fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeModel
#         fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = '__all__'


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookModel
#         fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        a = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        a.set_password(validated_data['password'])
        a.save()
        return a
