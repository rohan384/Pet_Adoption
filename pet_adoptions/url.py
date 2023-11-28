from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import (
#     PasswordResetView,
#     PasswordResetDoneView,
#     PasswordResetConfirmView,
#     PasswordResetCompleteView,
# )


urlpatterns = [
    path('home',views.home, name='home'),

    path('pet', views.pet_list, name='pet_list'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('adoption-records/', views.adoption_record_list, name='adoption_record_list'),
    path('pet/<int:pet_id>/adoption/', views.adoption_form, name='adoption_form'),
    path('donate', views.pet_donation, name='pet_donation'),

    path('blog', views.blog_entries, name='blog_entries'),
    path('blog/add/', views.add_blog_entry, name='add_blog_entry'),
    path('blog/edit/<int:entry_id>/', views.edit_blog_entry, name='edit_blog_entry'),
    # path('blog/delete/<int:entry_id>/', views.delete_blog_entry, name='delete_blog_entry'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Add URL patterns for adoption form, adoption record, etc.
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
]