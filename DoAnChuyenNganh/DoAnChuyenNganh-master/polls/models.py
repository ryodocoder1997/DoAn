from django.db import models


class PERSONALINFORMATION(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    avatar = models.ImageField()

    gender_choice = (
        ('M', 'Nam'),
        ('F', 'Nữ'),
    )
    gender = models.CharField(max_length=1, choices=gender_choice)
    date_of_birth = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=255)


def __str__(self):
    return self.id
