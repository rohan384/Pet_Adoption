from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Pet(models.Model):
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('U', 'Unknown'),
)
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    description = models.TextField()
    adoption_status = models.BooleanField(default=False)
    donated = models.BooleanField(default=False)

class AdoptionRecord(models.Model):
    adopter_name = models.CharField(max_length=255)
    contact_information = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Contact information must be 10 digits.',
                code='invalid_contact_information'
            )
        ]
    )
    email = models.EmailField(null=True, blank=False)
    adoption_date = models.DateField(auto_now_add=True)
    pet_adopted = models.ForeignKey('Pet', on_delete=models.CASCADE)

class BlogEntry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PetDonation(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
    )

    name = models.CharField(max_length=255)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gender')
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/', verbose_name='Pet Image')
    donater_name = models.CharField(max_length=25)
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[0-9]{10}$', message='Contact information must be a 10-digit number.')])
    email = models.EmailField()
