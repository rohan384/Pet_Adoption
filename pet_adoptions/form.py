from django import forms
from django.core.validators import RegexValidator
from .models import AdoptionRecord, Pet, BlogEntry, PetDonation
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AdoptionForm(forms.Form):
    adopter_name = forms.CharField(max_length=255, label='Your Name')
    contact_information = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10}$',
                message='Contact information must be a 10-digit number.',
            ),
        ]
    )
    email=forms.EmailField()

class PetDonationForm(ModelForm):
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('U', 'Unknown'),
)
    name = forms.CharField(max_length=255)
    species = forms.CharField(max_length=100)
    breed = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(label='Pet Image', required=True)
    donater_name=forms.CharField(max_length=25)
    contact_number = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10}$',
                message='Contact information must be a 10-digit number.',
            ),
        ]
    )
    email=forms.EmailField()

    class Meta:
        model = PetDonation
        fields = '__all__'



class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']