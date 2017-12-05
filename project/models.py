from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class User(AbstractUser):
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=12)
    picture = models.ImageField(blank=True)
    bio = models.CharField(max_length=300)


class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    people_choices = (
        (one, 'one person'), (two, 'two people'),
        (three, 'three people'), (four, 'four people'), (five, 'five  people')
    )
    people = models.CharField(
        max_length=1, choices=people_choices, default=one)
    time = models.TimeField()
    date_reserved = models.DateField()
    date_booked = models.DateTimeField(auto_now_add=True)
    pending = "pending"
    confirmed = "confirmed"
    status_choices = ((pending, "pending"), (confirmed, "confirmed"))
    status = models.CharField(
        max_length=10, choices=status_choices, default=pending)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
