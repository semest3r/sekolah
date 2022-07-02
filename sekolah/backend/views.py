from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class TestListView(ListView):
    model = Guru
    template_name = "backend/base.html"
  
class TestDetailView(DetailView):
    model = Guru
    template_name = "backend/detail.html"
    
class UserCreateView(CreateView):
    model = User    
    form_class = UserCreationForm
    success_url: reverse_lazy('dashboard')
    template_name = "backend/user.html"

