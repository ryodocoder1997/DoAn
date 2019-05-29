# Generated by Django 2.1.7 on 2019-05-13 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190509_1111'),
        ('polls', '0013_introductions_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_day', models.BooleanField()),
                ('monday_afternoon', models.BooleanField()),
                ('monday_night', models.BooleanField()),
                ('tuesday_day', models.BooleanField()),
                ('tuesday_afternoon', models.BooleanField()),
                ('tuesday_night', models.BooleanField()),
                ('wednesday_day', models.BooleanField()),
                ('wednesday_afternoon', models.BooleanField()),
                ('wednesday_night', models.BooleanField()),
                ('thursday_day', models.BooleanField()),
                ('thursday_afternoon', models.BooleanField()),
                ('thursday_night', models.BooleanField()),
                ('friday_day', models.BooleanField()),
                ('friday_afternoon', models.BooleanField()),
                ('friday_night', models.BooleanField()),
                ('saturday_day', models.BooleanField()),
                ('saturday_afternoon', models.BooleanField()),
                ('saturday_night', models.BooleanField()),
                ('sunday_day', models.BooleanField()),
                ('sunday_afternoon', models.BooleanField()),
                ('sunday_night', models.BooleanField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
    ]