from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='base'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
     path('delete/<int:id>/', views.deletefun, name="deletefun")
    ,path('update/<int:id>/', views.update, name="update"),
    path('showdata/',views.showform, name="addshow"),
    
]
