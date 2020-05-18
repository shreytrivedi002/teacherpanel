from django.contrib import admin
from django.conf import settings
from django.urls import path , include
from . import views 
from django.conf.urls.static import static




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
    path('coursesingle/<unqid>/<temail>', views.coursesingle , name='coursesingle' ),
    path('dashboard/coursesingle/<unqid>/<temail>', views.coursesingle , name='coursesingle' ),
    path('comment/', views.commentsave , name='commentsave' ),
    path('att/', views.att , name='att' ),
    path('dashboard/st_attendence/<temail>/<username>', views.st_attendence , name='st_attendence' ),
        # not used
    path('attpage/', views.attendencepage , name='attendencepage' ),
    path('profileupdate/', views.profileupdate , name='profileupdate' ),











    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)