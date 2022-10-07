from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('auth/', views.auth),
    path('reg/', views.reg),
    path('logout/', views.Distroy_Session),
    path('checkdata/', views.checkdata),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('create/', views.Create_Session),
    path('access/', views.Access_Session),
    path('distroy/', views.Distroy_Session),

]