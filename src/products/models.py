from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/<name>_<filename>
    return f'products/{instance.name}/{filename}'


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=user_directory_path, default="products/no_product_image.png")
    price = models.FloatField(help_text="in US dollars $")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"
