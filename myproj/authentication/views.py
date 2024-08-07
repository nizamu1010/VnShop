from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login



def index(request):
    return render (request, "index.html")


def signup(request):
    if request.method == 'POST':
        u_name = request.POST.get('username') 
        mail = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if u_name and mail and pass1 and pass2:
            if pass1 == pass2:
                if User.objects.filter(username=u_name).exists(): 
                    return redirect('authentication:signup')
                else:
                    user = User.objects.create_user(username=u_name, email=mail, password=pass1)
                    user.save()
                    return redirect('authentication:login')
            else:
                return redirect('authentication:signup')
        else:
            return redirect('authentication:signup')
    else:                
        return render(request, "signup.html")




from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        pass1 = request.POST.get('password')
        
        user = authenticate(request, username=u_name, password=pass1)
        
        if user is not None:
            auth_login(request, user)
            return redirect('authentication:index')
        else:
            return redirect('authentication:login')
        
    else:
        return render(request, "login.html")




def logout(request):
    auth.logout(request)
    return redirect('authentication:index')