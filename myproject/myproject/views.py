from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def fashion(request):
    return render(request,'fashion.html')

def electronic(request):
    return render(request,'ele.html')

def sports(request):
    return render(request,'sports.html')

def mobile(request):
    return render(request,'mobile.html')

def grocery(request):
    return render(request,'grocery.html')

def about(request):
    return render(request,'about.html')