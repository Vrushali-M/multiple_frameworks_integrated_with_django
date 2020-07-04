from django.shortcuts import render

# Create your views here.

def about_page(request):
    print(request.headers)
    return render(request, "about.html", {})