from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from account.views import hello_world, AccountCreateView

app_name='account'
urlpatterns = [
    path('', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]