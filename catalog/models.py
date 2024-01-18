from datetime import date

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import datetime
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(default=datetime.datetime.today)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="newspapers"
    )
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"{self.title} (topic: {self.topic.name}, published date: {self.published_date})"

    # def get_absolute_url(self):
    #     return reverse("catalog:newspaper-detail", args=[str(self.id)])


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"

    # def get_absolute_url(self):
    #     return reverse("catalog:redactor-detail", args=[str(self.id)])