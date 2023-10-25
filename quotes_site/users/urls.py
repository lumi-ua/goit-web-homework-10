from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterView



from . import views


app_name = "users"

urlpatterns = [
   
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'), name="logout")
 ]