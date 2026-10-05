from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# USER HOME
def home(request):

    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(
            pro_name__icontains=search
        )
    else:
        products = Product.objects.all()

    return render(request, 'home.html', {'products': products})

# PRODUCT DETAILS
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})


# ADMIN LIST
def admin_products(request):
    products = Product.objects.all()
    return render(request, 'admin_products.html', {'products': products})


# ADD
@login_required
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Product Added Successfully")
            return redirect('admin_products')

    else:
        form = ProductForm()

    return render(request, 'form.html', {'form': form})


# UPDATE
@login_required
def update_product(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Product Updated Successfully")
            return redirect('admin_products')

    else:
        form = ProductForm(instance=product)

    return render(request, 'form.html', {'form': form})


# DELETE
@login_required
def delete_product(request, id):

    product = get_object_or_404(Product, id=id)

    product.delete()

    messages.success(request, "Product Deleted Successfully")

    return redirect('admin_products')
def login_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('admin_products')

        else:
            messages.error(request, "Invalid username or password")


    return render(request, 'login.html')



def logout_user(request):

    logout(request)

    return redirect('login')