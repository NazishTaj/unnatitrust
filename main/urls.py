from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('university/', views.university, name='university'),
    path('registration/', views.registration, name='registration'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.termsandconditions, name='terms'),
    path('privacypolicy/' , views.privacypolicy, name='privacypolicy'),
    path('gallery/',views.gallery , name='gallery'),
    path('register/', views.student_registration, name='register'),
    path('success/', views.success_page, name='success'),

]
