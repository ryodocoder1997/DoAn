# Generated by Django 2.1.5 on 2019-03-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_studyprocess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(default=True, max_length=70, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('Skype', models.CharField(max_length=255)),
                ('Zalo', models.CharField(max_length=255)),
                ('Facebook', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('describe', models.TextField()),
                ('video', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
        migrations.RenameField(
            model_name='studyprocess',
            old_name='Educationlevel',
            new_name='Education_level',
        ),
    ]
