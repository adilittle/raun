from django.shortcuts import render

def myMainView(request):
    return render(request, "one.html")
