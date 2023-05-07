
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Quest(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        return self.description


