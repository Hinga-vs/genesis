from django.shortcuts import render, redirect, get_object_or_404
from Genesisapp.models import *

# Create your views here.
def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def home(request):
    if request.method =='POST':
        mycontact =contact1(
         name = request.POST['name'],
         email = request.POST['email'],
         subject = request.POST['subject'],
         message = request.POST['message'],   
         time = request.POST['time']
        )
        mycontact.save()
        return render(request, 'index.html')

        
    else:
        return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')



def show(request):
        all = contact1.objects.all()
        return render(request, 'show.html' , {'all':all})     #function to display a page for all info


def delete(request,id):
    mycontact = contact1.objects.get(id = id)
    mycontact.delete()
    return redirect('/show')

#function to edit ,update and replace the corrections made
def edit(request,id):
    editappointment = get_object_or_404(contact1, id=id)

    if request.method =='POST':
       editappointment.name = request.POST.get('name') 
       editappointment.email = request.POST.get('email') 
       editappointment.subject = request.POST.get('subject') 
       editappointment.message = request.POST.get('message') 
       editappointment.time = request.POST.get('time') 
       #that was the code to replace 
       editappointment.save()

       return redirect('/show')


    else:return render(request, 'edit.html', {'editappointment': editappointment})


