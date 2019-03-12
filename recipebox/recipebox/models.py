from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def url(self):
        return f"/author/{self.id}"


# class Food(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Unit(models.Model):
#     name = models.CharField(max_length=20)
#     abbr = models.CharField(max_length=6)

#     def __str__(self):
#         return self.name


class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    total_time = models.DurationField()
    instructions = models.TextField(default='')
    description = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.title

    def url(self):
        return f"/recipe/{self.id}"


# class Ingredient(models.Model):
#     qty = models.IntegerField()
#     unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=0, blank=True, null=True) # noqa
#     food = models.ForeignKey(Food, on_delete=models.CASCADE, default=0, blank=True, null=True) # noqa
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # noqa

#     def __str__(self):
#         return f"{self.qty} {self.unit} {self.food.name}"
