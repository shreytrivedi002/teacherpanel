from django.contrib import admin
from django.urls import path , include
from . import views 



urlpatterns = [

    path('', views.clghome , name='clghome' ),
    path('profile/', views.profile , name='profile' ),
    path('up/', views.up , name='up' ),
    path('dashboard/', views.dashboard , name='dashboard' ),
    # path('uploadprocess/', views.uploadprocess , name='uploadprocess' ),
    path('pdfs/', views.pdf , name='pdfs' ),
    path('updone/', views.updone , name='uploaddone' ),
    path('createuser/', views.createuser , name='createuser' ),
    path('signin/', views.signin , name='signin' ),
    path('signout/', views.signout , name='signout' ),







    


]