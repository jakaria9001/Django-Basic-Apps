from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

my_todos = [
    'Writing script for github readme.md',
    'Solve assignment problems', 
    'Learn Django details'
]
def index(request):
    return render(request, "todos.html", {
        'tasks': my_todos
    })
