from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


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


class Introductions(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.username.user.username


class Video(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.username.user.username


class Schedules(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)

    monday_day = models.BooleanField()
    monday_afternoon = models.BooleanField()
    monday_night = models.BooleanField()

    tuesday_day = models.BooleanField()
    tuesday_afternoon = models.BooleanField()
    tuesday_night = models.BooleanField()

    wednesday_day = models.BooleanField()
    wednesday_afternoon = models.BooleanField()
    wednesday_night = models.BooleanField()

    thursday_day = models.BooleanField()
    thursday_afternoon = models.BooleanField()
    thursday_night = models.BooleanField()

    friday_day = models.BooleanField()
    friday_afternoon = models.BooleanField()
    friday_night = models.BooleanField()

    saturday_day = models.BooleanField()
    saturday_afternoon = models.BooleanField()
    saturday_night = models.BooleanField()

    sunday_day = models.BooleanField()
    sunday_afternoon = models.BooleanField()
    sunday_night = models.BooleanField()

    def __str__(self):
        return self.username.user.username


class StudyProcess(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)
    training_center = models.CharField(max_length=255)
    gpa = models.DecimalField(blank=True, decimal_places=1, max_digits=11)
    edu_level = (
        ('Cao Đẳng', 'Cao Đẳng'),
        ('Đại Học', 'Đại Học'),
        ('Thạc Sỹ', 'Thạc Sỹ'),
        ('Tiến Sỹ', 'Tiến Sỹ'),
        ('Khác', 'Khác'),
    )
    education_level = models.CharField(max_length=15, choices=edu_level, default='Khác')
    country = CountryField(blank_label='(select country)')
    classification_level = (
        ('Xuất sắc', 'Xuất sắc'),
        ('Giỏi', 'Giỏi'),
        ('Khá', 'Khá'),
        ('Trung bình', 'Trung bình'),
    )
    classification = models.CharField(max_length=10, choices=classification_level, default='Khá')
    certificate = models.ImageField()
    training_time_start = models.DateField()

    def __str__(self):
        return self.username.user.username


class TypicalStudents(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    content = models.TextField(default='')

    def __str__(self):
        return self.username.user.username


class Classes(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=255)
    register_day = models.DateTimeField()
    address = models.CharField(max_length=255)
    start_day = models.DateTimeField()
    end_day = models.DateTimeField()
    tuition_fee = models.DecimalField(decimal_places=4, max_digits=8)
    maximum_student = models.IntegerField()
    registration_number = models.IntegerField()
    thumbnail = models.ImageField(null=False, default='')
    description = models.TextField(default='')
    status = (
        ('O', 'Bắt đầu chiêu sinh'),
        ('C', 'Ngưng chiêu sinh'),
        ('R', 'Đang dạy'),
        ('E', 'Kết thúc')
    )
    class_status = models.CharField(max_length=1, choices=status, default='C')

    def __str__(self):
        return self.username.user.username


class Courses(models.Model):
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.class_id


class Teachers(models.Model):
    username = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20)
    avatar = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.username.user.username
