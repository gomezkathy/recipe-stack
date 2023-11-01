from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    instructions = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        formatted_date = self.created_on.strftime("%d %b %Y")
        return f"{self.title} - ({formatted_date})"


class Playlist(models.Model):
    title = models.CharField(max_length=250)
    picture = models.URLField()
    recipes = models.ManyToManyField(Recipe)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return self.title
