from django.urls import path
from . import views


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('expense',views.expense,name='expense'),
    path('expens',views.expens,name='expens'),
    path('adexp',views.adexp,name='adexp'),
    path('edit/<int:pid>',views.edit,name='edit'),
    path('delete_it/<int:data_id>',views.delete_it,name="delete_it"),
    path('index1',views.index1,name='index1'),
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('',views.login),
]

