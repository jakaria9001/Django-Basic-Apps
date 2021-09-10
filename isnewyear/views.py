from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    # return HttpResponse("hello is new yr")
    return render(request, "isnewyear.html", {
        'day': datetime.now().day,
        'month': datetime.now().month,
        'year': datetime.now().year,
        'time': datetime.now().time,
    })