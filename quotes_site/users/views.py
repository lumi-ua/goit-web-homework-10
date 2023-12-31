from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.

from django.shortcuts import render, redirect
from django.views import View


from .forms import RegisterForm, LoginForm

# Create your views here.

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="app_quotes:main")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)



    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})
    

    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f'Ваш акаунт успішно створено: {username}')
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form}) 
    

def login_user(request):
    if request.user.is_authenticated:
        return redirect(to="app_quotes:main")
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="users:login")

        login(request, user)
        return redirect(to="app_quotes:main")

    return render(request, "users/login.html", context={"form": LoginForm()})








