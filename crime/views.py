from django.shortcuts import render, redirect,get_object_or_404
from .models import Crime
from django.core.paginator import Paginator
from django.contrib import messages
from CRMS.sessionFunc import sessions

# Create your views here.
def index(request):
    sessions(request)
    # add pagination
    condition = False
    if request.session['username']:
        crimes = Crime.objects.all()
        param = ""
        if request.method == "POST" and request.POST["search"]:
            param = request.POST["search"]
            
            if Crime.objects.filter(pk=param).exists():
                crimes = Crime.objects.filter(pk=param)
            else:
                condition = True
                
            
        paginator = Paginator(crimes, 10)
        pageNumber = request.GET.get('page')
        pageObj = paginator.get_page(pageNumber)
        
       
        context ={
            'crimes': pageObj,
            'searchparam':param,
            'con':condition,
            'pagecount': pageObj.paginator.page_range
        }
        return render(request, 'crime/index.html',context)
    else:
        return redirect("login")

def viewcrime(request, crimeid):
    if request.session['username']:
        crime = get_object_or_404(Crime, pk=crimeid)
        return render(request, 'crime/crimeform.html', {'crime':crime})

def deletecrime(request):
    # get the to delete
    key = request.GET.get('del')
    crime = Crime.objects.get(pk=key)
    crime.delete()
    return redirect("crime")

def search(request):
    if request.method =="POST":
        searchparametar = request.POST["search"]
    return 
    


def addcrime(request):
    sessions(request)
    if request.session["username"]:#check if login
        print(request.session['username'])
        if request.method == 'POST':
            title =request.POST['title']
            refno = request.POST['refno']
            section=request.POST['section']
            subsection = request.POST['subsection']
            acts = request.POST['Acts']
            charges = request.POST['charges']
            crimesave = Crime.objects.create(title=title, refno=refno, 
            section=section, subsection=subsection, acts=acts, charges=charges)
            crimesave.save()
            messages.success(request, "Record Saved")
            return redirect("crime")
    else:
        return redirect("login")
    return render(request, 'crime/crimeform.html')