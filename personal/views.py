from django.shortcuts import render
from django.conf import settings
# Create your views here.

def index(request):
    return render(request,'website/index.html',{
        'MEDIA_URL':settings.MEDIA_URL
    })