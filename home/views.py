from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    return render(request,"index.html")


def blog(request):
        
        return HttpResponse("Blog Page")    
    
def create(request):
            
            return HttpResponse("Create Page")
        
def profile(request):
                    
                    return HttpResponse("Profile Page")
                
def password(request):
                            
                            return HttpResponse("Password Page")                                
def login(request):
    
    return HttpResponse("Login Page")

def logout(request):
        
        return HttpResponse("Logout Page")

def delete(request):
            
            return HttpResponse("Delete Page")
        
def register(request):
                
                return HttpResponse("Register Page")    

def reset(request):
                        
                        return HttpResponse("Reset Page")   