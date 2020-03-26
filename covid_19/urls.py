from django.urls import path
from .views import covid_data

app_name = 'covid_19'

urlpatterns = [
    path('', covid_data)
]
