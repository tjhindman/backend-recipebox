from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbr = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    total_time = models.TimeField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    qty = models.IntegerField()
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE)
    food_id = models.OneToOneField(Food, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.food.name}"
