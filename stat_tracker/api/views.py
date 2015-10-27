from django.shortcuts import render

# Create your views here.
def basic(request):
    render(request, 'basic.html')
