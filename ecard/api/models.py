import uuid

from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_number = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    UID = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    access_level = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name
