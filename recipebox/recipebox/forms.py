from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
from recipebox.models import Author, User


class RecipeForm(forms.Form):

    author = forms.ChoiceField(choices=[])
    title = forms.CharField(max_length=120)
    total_time = forms.DurationField()
    instructions = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(max_length=300)

    def __init__(self, req, user_is_staff, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        if user_is_staff:
            self.choices = [
                (a.id, a.user.username) for a in Author.objects.all()]
        else:
            self.choices = [(req.user.id, req.user.username)]

        self.fields['author'] = forms.ChoiceField(choices=self.choices)


class AuthorForm(forms.Form):
    username = forms.CharField(max_length=40)
    bio = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=40)
#     password = kkk


# class SignupForm(forms.Form):
#     pass
