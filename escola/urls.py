from django.urls import path
from escola.views import home


urlpatterns = [
    path('', home),#home
]

