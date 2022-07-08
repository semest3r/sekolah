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
    #path("user/update/<pk>", UserUpdateView.as_view(), name='userUpdate'),
    #path("", loginView, name='loginView')
    path('user/delete/<pk>', UserDeleteView.as_view(), name="deleteView"),
    path('guru/', GuruView.as_view(), name="guruView"),
    path('guru/detail/<pk>', GuruDetailView.as_view(), name='guruDetail'),
    path('siswa/', SiswaView.as_view(), name="siswaView"),
    path('siswa/detail/<pk>', SiswaDetailView.as_view(), name='siswaDetail'),
    path('profile/<pk>', ProfileView.as_view(), name='profileView'),
    path('profile/update/<pk>', ProfileUpdate.as_view(), name='profileUpdate'),
]
