from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def longBoat(request):
    return HttpResponse('This is a good pub for Drinks')