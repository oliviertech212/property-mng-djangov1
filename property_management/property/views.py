from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

from .forms import LandlordRegisterForm, TenantRegisterForm
from .models import Property, Lease, User
from django.shortcuts import render, get_object_or_404
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('landlord_dashboard')  # Redirect to landlord dashboard
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})


def landlord_register(request):
    if request.method == 'POST':
        form = LandlordRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('landlord_dashboard')
    else:
        form = LandlordRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'Landlord'})

def tenant_register(request):
    if request.method == 'POST':
        form = TenantRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('tenant_dashboard')
    else:
        form = TenantRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'Tenant'})

@login_required
def admin_dashboard(request):
    properties = Property.objects.all()
    return render(request, 'admin_dashboard.html', {'properties': properties})
def admin_dashboard(request):
    context = {
        'total_properties': Property.objects.count(),
        'total_leases': Lease.objects.count(),
        'total_tenants': User.objects.filter(role='Tenant').count(),
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def landlord_dashboard(request):
    properties = request.user.properties.all()
    return render(request, 'landlord_dashboard.html', {'properties': properties})

@login_required
def tenant_dashboard(request):
    leases = request.user.leases.all()
    return render(request, 'tenant_dashboard.html', {'leases': leases})

def property_list(request):
    query = request.GET.get('q')
    properties = Property.objects.all()
    if query:
        properties = properties.filter(title__icontains=query)
    return render(request, 'property_list.html', {'properties': properties})


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})



def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})
