from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from sekolah.settings import LOGIN_REDIRECT_URL
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
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
        context['profile'] = self.request.user.id
        context['page_title'] = "Dashboard"
        return context
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class TestListView(ListView):
    model = User
    template_name = "backend/user.html"
    def get_context_data(self, **kwargs):
        context = super(TestListView, self).get_context_data(**kwargs)
        context['title'] = "List User"
        context['page_title'] = "List User"
        return context  
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class TestDetailView(DetailView):
    model = User
    template_name = "backend/detail.html"
    def get_context_data(self, **kwargs):
        context = super(TestDetailView, self).get_context_data(**kwargs)
        context['title'] = "Detail User"
        context['page_title'] = "Detail User"
        return context 
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class UserCreateView(CreateView):
    model = User    
    success_url = reverse_lazy('userView')
    template_name = "backend/register_user.html"
    form_class = UserCreationForm
    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = "Register"
        context['page_title'] = "Create User"
        return context

@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'backend/user_update.html'

    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('userView')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class GuruView(ListView):
    model = Guru
    template_name = 'backend/guru.html'
    def get_context_data(self, **kwargs):
        context = super(GuruView, self).get_context_data(**kwargs)
        context['title'] = "Guru"
        context['page_title'] = "List Guru"
        return context

@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class GuruDetailView(DetailView):
    model = Guru
    template_name = "backend/guru_detail.html"
    def get_context_data(self, **kwargs):
        context = super(GuruDetailView, self).get_context_data(**kwargs)
        context['title'] = "Detail Guru"
        context['page_title'] = "Detail Guru"
        return context   
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')   
class SiswaView(ListView):
    model = Siswa
    template_name = 'backend/siswa.html'
    def get_context_data(self, **kwargs):
        context = super(SiswaView, self).get_context_data(**kwargs)
        context['title'] = "Siswa"
        context['page_title'] = "List Siswa"
        return context    
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class SiswaDetailView(DetailView):
    model = Siswa
    template_name = "backend/siswa_detail.html"
    def get_context_data(self, **kwargs):
        context = super(SiswaDetailView, self).get_context_data(**kwargs)
        context['title'] = "Detail Siswa"
        context['page_title'] = "Detail Siswa"
        return context   
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class ProfileView(DetailView):
    model = User
    template_name = "backend/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['title'] = "Profile"
        context['page_title'] = "Profile"
        context['profile'] = self.request.user.id
        return context
    
@method_decorator(login_required(login_url=LOGIN_REDIRECT_URL), name='dispatch')
class ProfileUpdate(UpdateView):
    model = User
    template_name = "backend/edit_profile.html"
    success_url = reverse_lazy('welcome')
    fields = ['first_name', 'last_name']
    def get_context_data(self, **kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        context['title'] = "Profile"
        context['page_title'] = "Profile"
        return context 