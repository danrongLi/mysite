from django.http import HttpResponse

# Create your views here.
import random
def index(request):
    i=random.random()
    return HttpResponse('Hi! How are you!!!')

