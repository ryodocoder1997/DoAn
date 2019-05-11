# Generated by Django 2.1.7 on 2019-05-10 07:16

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190509_1111'),
        ('polls', '0011_userinfo_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.UserProfile')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(blank=True, max_length=255)),
                ('zalo', models.CharField(blank=True, max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.UserProfile'),
        ),
    ]
