from django.shortcuts import render

def index(request):
    """ Home page for the application """
    return render(request, "index.html")
    