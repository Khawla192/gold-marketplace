from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def store_index(request):
    return render(request, 'stores/index.html', {'stores': stores})

class Store:
    def __init__(self, picture, name, description, links, phone_number):
        self.picture = picture
        self.name = name
        self.description = description
        self.links = links
        self.phone_number = phone_number

stores = [
    Store(
        picture='main_app/static/images/mayar.jpeg',
        name='Mayar Jewellery',
        description='Description for Store 1',
        links=['maps.google.com/?q=26.219530%2C50.538277', 'https://www.instagram.com/mayarjewellery/?hl=en'],
        phone_number='12345890'
    ),
    Store(
        picture='main_app/static/images/alshehabi.jpeg',
        name='Alshehabi Jewllery',
        description='Description for Store 2',
        links=['linktr.ee/alshehabijewellery', 'https://www.instagram.com/alshehabijewellery/?hl=en'],
        phone_number='98743210'
    ),
    Store(
        picture='main_app/static/images/jaber.PNG',
        name='Jaber Jewellery',
        description='Description for Store 3',
        links=['linktr.ee/Jaber.jewellery', 'https://www.instagram.com/jaber.jewellery/?hl=en'],
        phone_number='55555555'
    ),
]

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
