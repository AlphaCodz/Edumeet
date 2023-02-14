from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, "index.html")
    
def Video(request):
    return render(request, "video.html")

def Departments(request):
    return render(request, "departments.html")