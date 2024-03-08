
from django.urls import path
from .views import home, logout_user, register_user

urlpatterns = [
    path('', home, name='home'),
    path('login/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

]