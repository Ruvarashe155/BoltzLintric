from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path(
    'projects/<int:pk>/',
    views.project_detail,
    name='project_detail'
),

]
