from django.http import HttpResponse
from .models import Pet
from django.shortcuts import render
# Create your views here.
import random
def index(request):
    i=random.random()
    return HttpResponse('Hi! How are you (i) !!!')

def all_pets(request):
    pets = Pet.objects.all()
    context = {
            'pets':pets,
            }
    return render(request, 'adopt/all.html',context)



def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)
