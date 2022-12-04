from django.shortcuts import render
from crime.models import *
from .models import  *

from django.contrib import messages
# Create your views here.

def index(request):
    criminal = Criminal.objects.all()
    return render(request, "criminal/index.html", {"criminals":criminal})

def search(request):
    if request.method == "POST":
        searchparam = request.POST["search"]
        print(searchparam)
        search = Criminal.objects.filter(pk=searchparam)
        context ={
            "search":search,
            "searchparam":searchparam
        }
    return render(request,"criminal/index.html", context )

def criminaladd(request):
    
    crime_option = Crime.objects.all()
    if request.method == "POST":

        selected_option = request.POST.get("crimeopt")
        fullname = request.POST["name"]
        nin = request.POST["nin"]
        crimeopt = request.POST["crimeopt"]
        charge = request.POST["charges"]
        image = request.FILES["src"]
        filtercrime= Crime.objects.get(pk=crimeopt)
        
        criminals = Criminal.objects.create(fullname=fullname, nin=nin, crime=filtercrime, image=image, charge=charge )
        criminals.save()
        messages.success(request, "Record Saved")


    return render(request, "criminal/criminalform.html", {"crimeoption": crime_option})


