# Generated by Django 4.0.5 on 2022-11-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='no_picture.png', upload_to='avatars'),
        ),
    ]
