from django import forms
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Form used for registering new Users
class RegistrationForm(UserCreationForm):
    email = forms.EmailField
    username = forms.CharField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # This data must be parsed into individual interest entities from the
    #   comma-separated charField.
    interest_input = forms.CharField(label="I like...", required=False)
    school = forms.ModelChoiceField(label="I attend...", queryset=School.objects.all())

    def clean(self):
        clean_data = super(RegistrationForm, self).clean()
        pass1 = clean_data.get("password1")
        pass2 = clean_data.get("password2")

        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match.")


