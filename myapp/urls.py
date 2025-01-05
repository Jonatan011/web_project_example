
from django.urls import path
from myapp.views import about, categories, contact, custom_login    
from myapp.views import home


urlpatterns = [
    path('', home, name='home'),  
    path('login/', custom_login, name='login'),
    path('categories/<str:name>', categories, name='categories'),  
    path('about/', about, name='about'),  
    path('contact/', contact, name='contact'),  


    #  path('singup/', custom_signup, name='singup'),

    
]

