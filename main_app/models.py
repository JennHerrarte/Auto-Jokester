from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

CATEGORIES = (
    'Random Jokes',
    'Yo Mama Jokes',
    'Dad Puns',
    'Knock Knock Jokes',
    'Bar Jokes',
    'Computer Jokes',
    'Sports Jokes',
    'Dog Jokes'
)

class Joke(models.Model):
    joke = models.CharField(max_length=10000) # what is the max length from the apis?
    
    source = models.CharField(max_length=50, blank=True, null=True,)

    favorites = models.ManyToManyField(User, blank=True, related_name = 'favorites')
    
    dislikes = models.ManyToManyField(User, blank=True, related_name = 'dislikes')

    category = models.CharField(max_length=50, choices=CATEGORIES, default=CATEGORIES[0])

    createdBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)

    appproved = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.joke}'