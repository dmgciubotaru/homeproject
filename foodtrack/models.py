from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.TextField(blank=True)
    duration = models.IntegerField(default=0)  # minutes
    rating = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
