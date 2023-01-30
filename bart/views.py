from django.shortcuts import render

# Create your views here.

#function to set cookies
def setcookies(request):
    response=render(request,'bart/setcookies.html')
    response.set_cookie('name','zaid')
    return response;
