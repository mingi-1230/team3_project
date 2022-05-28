from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import Join, Login


urlpatterns = [
    path('join/', Join.as_view(), name='join'),
    path('login/', Login.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]