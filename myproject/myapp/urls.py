from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='contact-page'),
    path('delete/<int:id>', views.deleteData, name='del-page'),
    path('update/<int:id>', views.updateData, name='upd-page'),
    path('reg/', views.userReg, name='reg-page'),
    path('login/', views.userLog, name='log-page'),
    path('logout/', views.userLogout, name='logout-page'),
    path('allitems/', views.allItems, name='items-page')
]