# Generated by Django 2.1.7 on 2019-05-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_remove_userinfo_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], max_length=3),
        ),
    ]
