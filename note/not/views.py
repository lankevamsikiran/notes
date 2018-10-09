from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def newproduct(request):
    return render(request, "newproduct.html")
