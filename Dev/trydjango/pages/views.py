from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"home.html",{})
    # return HttpResponse("<h1>Hello WOrld!</h1>")

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{})
