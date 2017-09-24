from django import forms
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Form used for registering new Users
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(initial="someone@example.com",
                             error_messages={'required': 'Please enter a valid email.',
                                             'invalid': 'This email is invalid.'})
    username = forms.CharField(max_length=50, initial="username", help_text="Must be unique.")
    password1 = forms.CharField(widget=forms.PasswordInput(), initial="enter a password",
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), initial="enter the password again",
                                label="Confirm Password")
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # This data must be parsed into individual interest entities from the
    #   comma-separated charField.
    interest_input = forms.CharField(label="Interests", initial="I like...", required=False)
    school = forms.ModelChoiceField(label="School", initial="I attend...", queryset=School.objects.all())

    def clean(self):
        clean_data = super(RegistrationForm, self).clean()
        pass1 = clean_data.get("password1")
        pass2 = clean_data.get("password2")

        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match.")
