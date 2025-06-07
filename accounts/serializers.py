from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model = CustomUser
           fields = ('id', 'username', 'email', 'phone_number', 'role')

class RegisterSerializer(serializers.ModelSerializer):
       password = serializers.CharField(write_only=True, min_length=8)
       password2 = serializers.CharField(write_only=True, min_length=8)

       class Meta:
           model = CustomUser
           fields = ('username', 'email', 'phone_number', 'role', 'password', 'password2')

       def validate(self, data):
           if data['password'] != data['password2']:
               raise serializers.ValidationError({"password": "Passwords must match."})
           return data

       def create(self, validated_data):
           validated_data.pop('password2')
           user = CustomUser.objects.create_user(
               username=validated_data['username'],
               email=validated_data['email'],
               phone_number=validated_data.get('phone_number', ''),
               role=validated_data.get('role', 'user'),
               password=validated_data['password']
           )
           return user