# Generated by Django 4.0.5 on 2022-11-15 15:01

import customers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(default='customers/no_picture.png', upload_to=customers.models.user_directory_path),
        ),
    ]