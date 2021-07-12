from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import SignupForm

# Create your views here.
def base_view(request):
    return HttpResponse("logged in")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/user/signup")
    else:
        form = SignupForm()

    return render(request, 'user/signup.html', {"form":form})

