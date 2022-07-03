from django import urls
from django.urls import path, include
from .views import*
from .views import UserCreateView


urlpatterns = [
    #path('', ModelView.as_view(), name='dashboard'),
    path('user/', TestListView.as_view(), name='userView'),
    path('user/detail/<pk>', TestDetailView.as_view(), name='detailView'),
    path("user/create/", UserCreateView.as_view(), name='createView'),
    #path("", loginView, name='loginView')

    
]
