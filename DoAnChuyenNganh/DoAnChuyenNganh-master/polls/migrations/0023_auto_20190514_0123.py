# Generated by Django 2.1.7 on 2019-05-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20190514_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyprocess',
            name='education_level',
            field=models.CharField(choices=[('Cao Đẳng', 'Cao Đẳng'), ('Đại Học', 'Đại Học'), ('Thạc Sỹ', 'Thạc Sỹ'), ('Tiến Sỹ', 'Tiến Sỹ'), ('Khác', 'Khác')], default='Khác', max_length=8),
        ),
    ]
