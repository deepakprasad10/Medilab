from django.urls import path
from .views import *
urlpatterns = [
    path('', view_Home, name='home'),
    path('service/', view_Service, name='Service'),
    path('about/', view_About, name='About'),
    path('testimonial/', view_Testimonial, name='Testimonial'),
    path('contact/', view_Contact, name='Contact'),
]
