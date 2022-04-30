
from django.urls import path
from medicalapp import views

app_name = 'medicalapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('about', views.about, name='about'),
    path('medicine', views.Medicine, name='Medicine'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('booking',views.booking,name='booking'),
    path('endpage', views.endpage, name='endpage')

]