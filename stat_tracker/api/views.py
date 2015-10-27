from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request, 'api/basic.html')
