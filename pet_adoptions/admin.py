from django.contrib import admin
from .models import Pet, AdoptionRecord, BlogEntry, PetDonation
from .form import PetDonationForm 
# Register your models here.
admin.site.register(Pet)
# admin.site.register(AdoptionRecord)

# class PetAdmin(admin.ModelAdmin):
#     list_display = ('name', 'species', 'breed', 'age', 'gender', 'adoption_status', 'display_image')

#     def display_image(self, obj):
#         return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

#     display_image.short_description = 'Image'

# admin.site.register(PetAdmin)

class AdoptionRecordAdmin(admin.ModelAdmin):
    list_display = ('adopter_name', 'contact_information', 'email', 'adoption_date', 'display_pet_name')

    def display_pet_name(self, obj):
        return obj.pet_adopted.name

    display_pet_name.short_description = 'Pet Adopted'

class PetDonationAdmin(admin.ModelAdmin):
    form = PetDonationForm 

admin.site.register(AdoptionRecord, AdoptionRecordAdmin)
admin.site.register(BlogEntry)
admin.site.register(PetDonation, PetDonationAdmin)