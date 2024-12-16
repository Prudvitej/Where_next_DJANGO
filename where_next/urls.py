from django.contrib import admin
from django.urls import path
from main import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('home/', RedirectView.as_view(url='/', permanent=False), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('details/', views.events_details, name='events_details'),
    path('thanks/', views.thanks, name='thanks'),
]
