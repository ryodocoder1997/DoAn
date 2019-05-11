from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserInfo(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField()

    gender_choice = (
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    )
    gender = models.CharField(max_length=3, choices=gender_choice, default='Nam')
    date_of_birth = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.username.user.username


class Contacts(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE, primary_key=True)
    phone_number = PhoneNumberField(blank=False, unique=True)
    address = models.CharField(max_length=255, blank=False)
    skype = models.CharField(max_length=255, blank=True)
    zalo = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username.user.username
