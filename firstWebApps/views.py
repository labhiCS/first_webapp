from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for firstWebApp"""
    return render(request, 'firstWebApps/index.html')