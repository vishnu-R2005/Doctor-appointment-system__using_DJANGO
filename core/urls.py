from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),   # homepage
    # path('/',views.home),
    path('home/', views.home, name='home'),
    path("delete/<int:id>/",views.del_appointments, name="delete"),
    path('edit/<int:id>/', views.edit_appointment, name='edit'),
    path('register', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
