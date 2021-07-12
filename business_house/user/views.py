from django.http import HttpResponse

# Create your views here.
def base_view(request):
    return HttpResponse("logged in")

