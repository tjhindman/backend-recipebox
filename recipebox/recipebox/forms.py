from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
from recipebox.models import Author, User


class RecipeForm(forms.Form):
    author = forms.ChoiceField(
        choices=[(a.id, a.user.username) for a in Author.objects.all()])
    title = forms.CharField(max_length=120)
    total_time = forms.DurationField()
    instructions = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(max_length=300)

    def clean_recipe_data(self):
        pass


class AuthorForm(forms.Form):
    username = forms.CharField(max_length=40)
    bio = forms.CharField(widget=forms.Textarea)
