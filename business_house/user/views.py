from django.shortcuts import redirect, render
from .forms import SignupForm
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        wallet = models.Wallet.objects.get(user_id=request.user.id)
        credit = wallet.credit
        username = request.user.username

        return render(request, 'user/home.html', {"credit":credit, "username":username})
    return render(request, 'user/home.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            user = User.objects.get(username = username)
            wallet = models.Wallet(user_id=user)
            wallet.save()
        return redirect("/user/signup")
    else:
        form = SignupForm()

    return render(request, 'user/signup.html', {"form":form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.

