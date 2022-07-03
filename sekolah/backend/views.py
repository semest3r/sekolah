from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from sekolah.settings import LOGIN_REDIRECT_URL
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
        'page_title' : 'Login',
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
                messages.info(request, 'Username OR Password SALAH TOLOL')
    return render(request, 'backend/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('loginView')

class HomeView(TemplateView):
    template_name = "backend/welcome.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home"
        context['page_title'] = "Home"
        return context
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class TestTemplateView(TemplateView):
    template_name = "backend/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Dashboard"
        context['page_title'] = "Dashboard"
        return context
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class TestListView(ListView):
    model = User
    template_name = "backend/base.html"
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class TestDetailView(DetailView):
    model = User
    template_name = "backend/detail.html"
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class UserCreateView(CreateView):
    model = User    
    success_url = reverse_lazy('userView')
    template_name = "backend/user.html"
    form_class = UserCreationForm
    
    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = "Register"
        context['page_title'] = "Create User"
        return context    
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('userView')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

class GuruView(ListView):
    model = Guru
    template_name = 'backend/guru.html'
    def get_context_data(self, **kwargs):
        context = super(GuruView, self).get_context_data(**kwargs)
        context['title'] = "Guru"
        context['page_title'] = "List Guru"
        return context
    
class SiswaView(ListView):
    model = Siswa
    template_name = 'backend/siswa.html'
    def get_context_data(self, **kwargs):
        context = super(SiswaView, self).get_context_data(**kwargs)
        context['title'] = "Siswa"
        context['page_title'] = "List Siswa"
        return context    