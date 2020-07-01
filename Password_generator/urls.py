from django.urls.conf import path, include
from Password_generator import views

urlpatterns = [
    path('passwordgenerated/', views.home, name= 'password'),
    path('about/', views.about, name='about'),
    path('newpassword/', views.results, name='results'),

]