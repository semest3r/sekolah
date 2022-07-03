from unicodedata import name
from django import urls
from django.urls import path, include
from .views import*


urlpatterns = [
    #path('', ModelView.as_view(), name='dashboard'),
    path("", TestTemplateView.as_view(), name='welcome'),
    path('user/', TestListView.as_view(), name='userView'),
    path('user/detail/<pk>', TestDetailView.as_view(), name='detailView'),
    path("user/create/", UserCreateView.as_view(), name='createView'),
    #path("", loginView, name='loginView')
    path('user/delete/<pk>', UserDeleteView.as_view(), name="deleteView"),
    path('guru/', GuruView.as_view(), name="guruView"),
    path('siswa/', GuruView.as_view(), name="siswaView"),
]
