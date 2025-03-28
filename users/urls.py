from django.urls import path
from users.views import login_view, register

urlpatterns = [
    path('login', login_view, name='login_view'),
    path('register', register, name='register'),
]