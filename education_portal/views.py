from django.shortcuts import render
from .models import Service, ServiceCategory
from.models import HomePageImages
def homepage(request):
    images = HomePageImages.objects.first()
    services = Service.objects.all()
    context = {
        'services': services,
        'images' : images,
    }
    return render(request, 'education_portal/homepage.html', context)


def landing_page(request):
    
    
    return render(request, "LandingPage_Final.html")

