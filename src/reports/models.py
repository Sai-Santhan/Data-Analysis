from django.db import models
from django.urls import reverse

from profiles.models import Profile


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/reports/user_<id>/<filename>
    return f'reports/user_{instance.author.user.id}/{filename}'


class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("reports:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["-created"]
        unique_together = ["name", "remarks", "author"]
