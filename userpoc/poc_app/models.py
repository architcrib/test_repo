__author__ = 'archit'

from django.db import models
from django.contrib.auth.models import AbstractUser


class CribUser(AbstractUser):
    phone_no = models.CharField(max_length=30, unique=True)
    is_tenant = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)


class Operator(models.Model):
    user = models.OneToOneField(CribUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    roles = models.Choices('warden', 'manager', 'owner')

    objects = models.Manager()

    def __str__(self):
        return self.name


class Tenant(models.Model):
    user = models.OneToOneField(CribUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=False)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

    objects = models.Manager()
