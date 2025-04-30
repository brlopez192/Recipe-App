from django.db import models
from django.shortcuts import reverse

# Create your models here.

difficulity_choices = (
    ('easy', 'Easy'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard')
)


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField(default='No ingredients')
    cooking_time = models.IntegerField()
    difficulty = models.CharField(
        max_length=12,
        choices=difficulity_choices,
        default='easy'
    )
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
  
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})
