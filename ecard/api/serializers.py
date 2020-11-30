import uuid

from rest_framework import serializers
from .models import Employee
from django.contrib.auth.hashers import make_password


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Employee
        fields = ['name', 'last_name', 'employee_number', 'password', 'email', 'UID', 'access_level']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(EmployeeSerializer, self).create(validated_data)

# class EmployeeSerializer(serializers.Serializer):
#    name = serializers.CharField(max_length=50)
#    last_name = serializers.CharField(max_length=50)
#    employee_number = serializers.IntegerField()
#    password = serializers.CharField(write_only=True, required=True)
#    email = serializers.EmailField(max_length=100)
#    UID = serializers.UUIDField(default=uuid.uuid4)
#    access_level = serializers.IntegerField(default=False)

#    def create(self, validated_data):
#        validated_data['password'] = make_password(validated_data.get('password'))
#        return Employee.objects.create(validated_data)

#    def update(self, instance, validated_data):
#        instance.name = validated_data.get('name', instance.name)
#        instance.last_name = validated_data.get('last_name', instance.last_name)
#        instance.employee_number = validated_data.get('employee_number', instance.employee_number)
#        instance.email = validated_data.get('email', instance.email)
#        instance.UID = validated_data.get('UID', instance.UID)
#        instance.access_level = validated_data.get('access_level', instance.access_level)
#        instance.save()
#        return instance
