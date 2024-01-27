from django.shortcuts import render

# Create your views here.
def főoldal(request):
    return render(request,"főoldal.html")