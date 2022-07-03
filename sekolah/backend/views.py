from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
    
def loginView(request):
    context = {
        'page_title' : 'Home',
    }
    if request.user.is_authenticated:
        return redirect('welcome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'backend/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('loginView')
  
@method_decorator(login_required, name='dispatch')
class TestListView(ListView):
    model = User
    template_name = "backend/base.html"
  
class TestDetailView(DetailView):
    model = User
    template_name = "backend/detail.html"
    
class UserCreateView(CreateView):
    model = User    
    form_class = UserCreationForm
    success_url = reverse_lazy('userView')
    template_name = "backend/user.html"

