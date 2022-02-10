from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Donate
from datetime import datetime
# Create your views here.
def home(request):
    return render (request,'home.html')
@login_required(login_url='auth/login')
def donate(request):
    bloodgroups =['A+','B+','AB+','AB-','O+','O-']
    states = [ "Andhra Pradesh",
                "Arunachal Pradesh",
                "Assam",
                "Bihar",
                "Chhattisgarh",
                "Goa",
                "Gujarat",
                "Haryana",
                "Himachal Pradesh",
                "Jammu and Kashmir",
                "Jharkhand",
                "Karnataka",
                "Kerala",
                "Madhya Pradesh",
                "Maharashtra",
                "Manipur",
                "Meghalaya",
                "Mizoram",
                "Nagaland",
                "Odisha",
                "Punjab",
                "Rajasthan",
                "Sikkim",
                "Tamil Nadu",
                "Telangana",
                "Tripura",
                "Uttarakhand",
                "Uttar Pradesh",
                "West Bengal",
                "Andaman and Nicobar Islands",
                "Chandigarh",
                "Dadra and Nagar Haveli",
                "Daman and Diu",
                "Delhi",
                "Lakshadweep",
    
                "Puducherry"]

    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       age = request.POST.get('age')
       gender = request.POST.get('gender')
       choose = request.POST.get('choose')
       bloodgroups = request.POST.get('bloodgroups')
       state = request.POST.get('state')
       mobile = request.POST.get('mobile')
       address = request.POST.get('address')
       issues = request.POST.get('issues')

       donate = Donate(name=name, email=email, age=age, gender=gender,choose=choose, blood_group=bloodgroups,state=state, mobile=mobile, address=address, issues=issues,posted_at=datetime.now(),is_published=True,author=request.user)
       donate.save()


    return render (request,'donate.html',context = {'bloodgroups':bloodgroups,'states':states})
def receive_detail(request,title):
    ddata = Donate.objects.get(donate_id=title)
    return render (request,'receive_detail.html',context = {'i': ddata,})


def receive(request):
    data = Donate.objects.all()
    print(data)
    return render (request,'receive.html',context = {'data': data,})
    
def receive_state(request):
    if request.method == 'POST':
        state=request.POST.get('state')

    data = Donate.objects.all()
    print(data)
    return render (request,'receive.html',context = {'data': data,})  

def receive_group(request):
    data = Donate.objects.all()
    print(data)
    return render (request,'receive.html',context = {'data': data,})

def receive_choose(request):
    data = Donate.objects.all()
    print(data)
    return render (request,'receive.html',context = {'data': data,})          