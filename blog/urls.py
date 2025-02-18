from django.urls import path
from .views import hello, index

# creating urls
urlpatterns = [
    path('', hello)
]
urlpatterns = [
    path('', index)
]
