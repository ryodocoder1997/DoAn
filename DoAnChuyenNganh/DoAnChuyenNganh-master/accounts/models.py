from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    level = (
        ('G', 'Vàng'),
        ('S', 'Bạc'),
        ('D', 'Mặc định'),
    )
    account_level = models.CharField(max_length=1, choices=level,
                                     default='D')

    type = (
        ('A', 'Trung Tâm'),
        ('S', 'Học sinh'),
        ('T', 'Gia sư'),
    )
    account_type = models.CharField(max_length=1, choices=type,
                                    default='S')

    is_agreed = models.BooleanField()

    def __str__(self):
        return self.user.username
