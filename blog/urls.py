from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('update/<str:pk>/', views.updatePage, name='update'),
    path('edit/<str:pk>/', views.editBlog, name='edit'),
]
