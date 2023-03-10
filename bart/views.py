from django.shortcuts import render

# Create your views here.

#function to set cookies
def setcookies(request):
    response=render(request,'bart/setcookies.html')
    response.set_cookie('name','zaid')
    return response;

#function for get cookies
def getcookies(request):
    name=request.COOKIES.get('name','zaid as guest')
    return render(request,'bart/getcookies.html',{'name':name})

#function for deleting cookies from terminal
def deletecookies(request):
    response=render(request,'bart/deletecookies.html')
    response.delete_cookie('name')
    return response
