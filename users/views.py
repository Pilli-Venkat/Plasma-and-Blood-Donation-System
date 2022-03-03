from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
    
            return redirect('home')
    return render(request, 'login.html')     

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username=email, first_name=username,last_name=lname, email=email, password=password1)
            user.save()
            return redirect('login')


        
    return render(request, 'signup.html')    


def logout_view(request):
    logout(request)
    return redirect('home')
    