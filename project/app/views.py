from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Donate
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
    return render (request,'donate.html',context = {'bloodgroups':bloodgroups,'states':states})

def receive(request):
    data = Donate.objects.all()
    print(data)
    return render (request,'receive.html',context = {'data': data,})