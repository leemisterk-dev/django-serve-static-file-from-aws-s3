from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CarList.as_view(), name='car-list'),
]
