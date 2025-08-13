from django.shortcuts import render
from django.conf import settings
from .models import User,Product
# Create your views here.

def index(request):
    user = User.objects.all()
    return render(request,'website/index.html',{
        'MEDIA_URL':settings.MEDIA_URL,
        'users':user
    })