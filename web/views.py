from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    proyectos = Project.objects.all()
    context = {
        "proyectos": proyectos
    }
    return render(request, 'pages/index.html', context)