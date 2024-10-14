from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import ProductForm

from django.shortcuts import render, redirect
from .forms import ProductForm


def index(request):
    return render(request, 'index.html')  # Adjust 'craft' to your app's name

def home(request):
    return render(request, 'home.html')  # Adjust 'craft' to your app's name

def vendor(request):
    return render(request, 'vendor.html')  # Adjust 'craft' to your app's name

# myapp/views.py


def register(request):
    if request.method == 'POST':
        username = request.POST.get('txt')  # User name
        email = request.POST.get('email')
        password = request.POST.get('pswd')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose a different one.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return redirect('register')

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful! You can log in now.')
            return redirect('login')  # Redirect to login page
        except Exception as e:
            messages.error(request, f'Error creating user: {str(e)}')
            return redirect('register')

    return render(request, 'register.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Change to your desired redirect
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'Logged out successfully!')
        return redirect('index')
    return render(request, 'logout.html')


# vendor/views.py




def velog(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('vendor')  # Change to your desired redirect
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'velog.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('txt')  # User name
        email = request.POST.get('email')
        password = request.POST.get('pswd')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose a different one.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return redirect('signup')

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful! You can log in now.')
            return redirect('velog')  # Redirect to login page
        except Exception as e:
            messages.error(request, f'Error creating user: {str(e)}')
            return redirect('signup')

    return render(request, 'signup.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendor')  # Ensure 'vendor' is a valid URL name
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})





def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list or a specific page
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'edit_product.html', {'form': form, 'product': product})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        fform = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list or a specific page
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'edit_product.html', {'form': form, 'product': product})



# views.py



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})



