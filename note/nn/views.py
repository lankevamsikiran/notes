from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def newproduct(request):
    return render(request, "newproduct.html")
def saveproduct(request):
    pid=request.POST['pid']
    pname=request.POST['pname']
    p=product(pid,pname)
    p.save()
    return render(request, 'index.html')
