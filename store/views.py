from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import SupplyForm, SignUpForm
from .models import Supply


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('dashboard')  
            else:
                login(request, user)
                return redirect('school_supply')
        else:
            # Handle invalid login credentials
            return render(request, 'store/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'store/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('school_supply')
    else:
        form = SignUpForm()

    return render(request, 'store/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('school_supply')

def school_supply(request):
    supplys = Supply.objects.all()
    return render(request, 'store/school_supply.html', {'supplys': supplys})

def supply_detail(request, pk):
    supply = get_object_or_404(Supply, pk=pk)
    return render(request, 'store/supply_detail.html', {'supply': supply})


def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def dashboard(request):
    supplys = Supply.objects.all()
    return render(request, 'store/dashboard.html', {'supplys': supplys})


@user_passes_test(is_admin)
def add_supply(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('school_supply')
    else:
        form = SupplyForm()
    return render(request, 'store/add_supply.html', {'form': form})

@user_passes_test(is_admin)
def edit_supply(request, pk):
    supply = get_object_or_404(Supply, pk=pk)
    if request.method == 'POST':
        form = SupplyForm(request.POST, request.FILES, instance=supply)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SupplyForm(instance=supply)
    return render(request, 'store/edit_supply.html', {'form': form, 'supply': supply})

@user_passes_test(is_admin)
def delete_supply(request, pk):
    supply = get_object_or_404(Supply, pk=pk)
    if request.method == 'POST':
        supply.delete()
        return redirect('dashboard')

