from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path("delete/<int:id>/",views.del_appointments, name="delete")
]
