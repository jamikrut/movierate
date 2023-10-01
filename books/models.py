from django.db import models


class PublishPlace(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    publish_date = models.DateField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=1)
    vote_count = models.IntegerField()
    publish_place = models.OneToOneField(PublishPlace, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
