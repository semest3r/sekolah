from django import urls
from django.urls import path
from .views import*
from .views import  UserCreateView

urlpatterns = [
    path("", TemplateView.as_view(template_name='backend/welcome.html'), name="welcome"),
    #path('', ModelView.as_view(), name='dashboard'),
    path('user/', TestListView.as_view(), name='dashboard'),
    path('user/detail/<pk>', TestDetailView.as_view(), name='dashboard'),
    path("user/create/", UserCreateView.as_view())
]
