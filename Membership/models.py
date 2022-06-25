from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    personal_address = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20, blank=False)
    gender = models.CharField(max_length=10, blank=False)
    gym_name = models.CharField(max_length=150, blank=False)
    gym_location = models.CharField(max_length=100, blank=False)
    gym_phone = models.CharField(max_length=20, blank=False)


class Membership(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    membership_type = models.CharField(max_length=100, blank=False)
    membership_price = models.IntegerField(blank=False)
    membership_duration = models.CharField(max_length=20, blank=False)

    def __str__(self):
        if self.membership_duration == "1" :
            return f"{self.membership_type} for {self.membership_duration} month"
        else:
            return f"{self.membership_type} for {self.membership_duration} months"


class Members(models.Model):
    gym_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='gym_owner', default=None)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=10, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=100, blank=False)
    membership = models.ForeignKey(
        Membership, on_delete=models.CASCADE, related_name='membership')
    validity = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def is_valid(self):
        return date.today() < self.validity