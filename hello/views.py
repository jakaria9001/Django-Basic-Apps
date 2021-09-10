from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")
def greet(request, name):
    # return HttpResponse(f"Hello { name.upper() }")
    return render(request, "index.html", {'user_name' : name})
