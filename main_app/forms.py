from django.forms import ModelForm
from .models import Joke

class JokeForm(ModelForm):
  class Meta:
    model = Joke
    fields = [
        'joke', 
        'source', 
        'category', 
        'createdBy',
        ]
