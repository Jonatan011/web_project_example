from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from .forms import CustomAuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})  


def about(request):
    return render(request, 'myapp/about.html')  

def contact(request):
    return render(request, 'myapp/contact.html')  



def home(request):
    return render(request, 'myapp/home.html')  


def categories(request, name):
    categories = ["category1", "category2", "category3", "category4", "category5","code"]
    context= {"name": name, "categories": categories}
    return render(request, 'myapp/categories.html', context)