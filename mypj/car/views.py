from django.shortcuts import render
from django.views import View
from .models import Car

# Create your views here.


class CarList(View):
    def get(self, request):

        cars = Car.objects.all()


        return render(request, 'car/car_list.html',{"cars":cars})

