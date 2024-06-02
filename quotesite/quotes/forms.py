from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import *

class TagForm(ModelForm):
    tag = CharField(min_length=3, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']
    
class QuoteForm(ModelForm):
    quote= CharField(min_length=3, max_length=1350, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = [ 'author', 'tags']
    

class AuthorForm(ModelForm):
    fullname = CharField(min_length=2, max_length=50, required=True, widget=TextInput())
    born_date= CharField(min_length=2, max_length=50, required=True, widget=TextInput())
    born_location= CharField(min_length=2, max_length=80, required=True, widget=TextInput())
    description= CharField(min_length=2, required=True, widget=Textarea(attrs={'cols': 40}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']