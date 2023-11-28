from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Pet, AdoptionRecord, BlogEntry
from .form import AdoptionForm, PetDonationForm, BlogEntryForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def pet_list(request):
    query = request.GET.get('q')
    if query:
        pets = Pet.objects.filter(Q(species__icontains=query) | Q(breed__icontains=query), adoption_status=False)
    else:
        pets = Pet.objects.filter(adoption_status=False)
    return render(request, 'pet_adoptions/pet_list.html', {'pets': pets, 'query': query, 'msg':'No result'})

@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request,'pet_adoptions/pet_detail.html',{'pet': pet})

# Add views for adoption form, adoption record, etc.
@login_required
def adoption_form(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            adopter_name = form.cleaned_data['adopter_name']
            contact_info = form.cleaned_data['contact_information']
            email = form.cleaned_data['email']
            # Create AdoptionRecord
            adoption_record = AdoptionRecord.objects.create(
                adopter_name=adopter_name,
                contact_information=contact_info,
                email=email,
                pet_adopted=pet
            )
            # Update Pet adoption status
            pet.adoption_status = True
            pet.save()
            return render(request, 'pet_adoptions/adoption_success.html', {'adoption_record': adoption_record})
    else:
        form = AdoptionForm()
    return render(request, 'pet_adoptions/adoption_form.html', {'form': form, 'pet': pet})

@login_required
def adoption_record_list(request):
    adoption_records = AdoptionRecord.objects.all()
    return render(request, 'pet_adoptions/adoption_record_list.html', {'adoption_records': adoption_records})

@login_required
def pet_donation(request):
    if request.method == 'POST':
        form = PetDonationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new pet instance with the donated information
            new_pet = Pet.objects.create(
                name=form.cleaned_data['name'],
                species=form.cleaned_data['species'],
                breed=form.cleaned_data['breed'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                donated=True  # Mark the pet as donated
            )

            # Redirect to a thank-you page or display a success message
            return render(request, 'pet_adoptions/donation_success.html', {'new_pet': new_pet})
    else:
        form = PetDonationForm()

    return render(request, 'pet_adoptions/pet_donation.html', {'form': form})

@login_required
def blog_entries(request):
    blog_entries = BlogEntry.objects.all().order_by('-created_at')
    return render(request, 'pet_adoptions/blog_entries.html', {'blog_entries': blog_entries})

@login_required
def add_blog_entry(request):
    if request.method == 'POST':
        form = BlogEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('blog_entries')
    else:
        form = BlogEntryForm()

    return render(request, 'pet_adoptions/add_blog_entry.html', {'form': form})

@login_required
def edit_blog_entry(request, entry_id):
    entry = get_object_or_404(BlogEntry, pk=entry_id)
    if request.method == 'POST':
        form = BlogEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('blog_entries')
    else:
        form = BlogEntryForm(instance=entry)

    return render(request, 'pet_adoptions/edit_blog_entry.html', {'form': form, 'entry': entry})

# @login_required
# def delete_blog_entry(request, entry_id):
#     entry = get_object_or_404(BlogEntry, pk=entry_id)
#     if request.method == 'POST':
#         entry.delete()
#         return redirect('blog_entries')

#     return render(request, 'pet_adoptions/delete_blog_entry.html', {'entry': entry})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL you want to redirect to after login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
