from django.urls import path

# Importing the homePageView function from the views.py in the current directory.
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]