from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Cart, CartItem
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import StaffSignupForm, StaffLoginForm
from .models import CartItem
from .forms import ProductForm
from .models import Product
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import CartItem, Product


def index(request):
    products = Product.objects.all()
    star_range = range(1, 6)  # This creates a range of 1 to 5
    return render(request, 'index.html', {'products': products, 'star_range': star_range})





def product_list(request):
    products = Product.objects.all()  # Get all products from the database
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for image upload
        if form.is_valid():
            form.save()
            return redirect('accounts:product_list')  # Adjust this to your actual product list view name
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})



def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # This will return a 404 if the product doesn't exist
    product.delete()
    return redirect('accounts:product_list')  # Redirect to the product list after deletion

# views.pyfrom django.shortcuts import render, redirect


def staff_signup(request):
    if request.method == 'POST':
        form = StaffSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('accounts:staff_login')  # Redirect to login after signup
    else:
        form = StaffSignupForm()
    
    return render(request, 'staff_signup.html', {'form': form})

def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:product_list')  # Ensure this URL pattern exists
            else:
                # Invalid login
                form.add_error(None, "Invalid username or password.")
    else:
        form = StaffLoginForm()
    
    return render(request, 'staff_login.html', {'form': form})

def staff_logout(request):
    logout(request)
    return redirect('accounts:staff_login')  # Redirect to login after logout



def home(request):
    products = Product.objects.filter(is_approved=True)
    star_range = range(1, 6)  # This creates a range of 1 to 5
    return render(request, 'home.html', {'products': products, 'star_range': star_range})  

    
    

def search_view(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'index.html', {'products': results})

def search_viewH(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'home.html', {'products': results})



def about(request):
    return render(request,'about.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:home')  # Redirect to a home page or dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



# views.py



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Create cart if it doesn't exist

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:  # If the item is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('accounts:cart_view')  # Redirect to cart view


def cart_view(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]  # Get or create the user's cart
    cart_items = CartItem.objects.filter(cart=cart)  # Fetch cart items for the user's cart
    total = sum(item.product.price * item.quantity for item in cart_items)  # Calculate total

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
    })

# views.py


def delete_cart_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.delete()
        return redirect('accounts:cart_view')  # Redirect to the cart view after deletion

from django.views.generic import DetailView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'



def edit_product(request, product_id):
    # Retrieve the product or return a 404 error if not found
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # Get data from the form
        product.name = request.POST.get('name', product.name)
        product.price = request.POST.get('price', product.price)
        product.slogan = request.POST.get('slogan', product.slogan)
        product.description = request.POST.get('description', product.description)

        # Handle image upload if provided
        if 'image' in request.FILES:
            product.image = request.FILES['image']

        # Save the updated product
        try:
            product.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('accounts:product_list')  # Redirect to the product list
        except Exception as e:
            messages.error(request, f'Error updating product: {str(e)}')

    # Render the edit product template with the product instance
    return render(request, 'edit_product.html', {'product': product})




def create_order(request):
    api_key = settings.RZP_TEST_API_KEY
    api_secret = settings.RZP_TEST_API_SECRET

    print(f"Using API Key: {api_key}")

    client = razorpay.Client(auth=(api_key, api_secret))
    
    # Example total amount; this can be dynamically set based on user input
    total_amount = 500  # Amount in INR
    data = {
        "amount": total_amount * 100,  # Convert to paise
        "currency": "INR",
        "receipt": "receipt#1",
        "payment_capture": 1  # Auto capture
    }
    
    try:
        order = client.order.create(data=data)
        return JsonResponse(order)
    except Exception as e:
        print(f"Error creating order: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))

        # Update the cart item quantity
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.quantity = quantity
        cart_item.save()

        # Calculate the new total
        total = sum(item.product.price * item.quantity for item in CartItem.objects.all())

        return JsonResponse({'total': total})

    return JsonResponse({'error': 'Invalid request'}, status=400)



