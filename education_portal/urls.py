from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("landing_page/", views.landing_page, name="landing_page"),
    
]
