from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/customers/username_<filename>
    return f'customers/{instance.name}_{filename}'


class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to=user_directory_path, default='customers/no_picture.png')

    def __str__(self):
        return str(self.name)
