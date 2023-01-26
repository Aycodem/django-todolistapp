from django.shortcuts import render,redirect
from .models import Note
from .serializer import *
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .decorators import *
from django.contrib.auth.decorators import login_required 

# Create your views here

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def createnote(request):
    if request.method == "POST":
        text =request.POST['text']
        if text!= "" :
            note=Note()
            note.text=text
            note.save()
            return redirect('/') 
            
        else:
            messages.info(request,'*Please Input some values')
        return redirect('/') 

    if request.method == 'GET': 
        text=Note.objects.all()
        # text=Note.objects.filter(customer__user='Haywhy')
        notes={'notes':text}
        return render(request,'To do list app.html',notes)
    return render(request,'To do list app.html')


def delete(request,pk):
    textnote=Note.objects.get(id=pk)
    textnote.delete()
    return redirect('/')

def update(request,pk):
    text=Note.objects.get(id=pk)
    if request.method=="POST":
        context=NoteSerializer(instance=text,data=request.POST)
        if context.is_valid():
            context.save()
            return redirect('/')
    if request.method == "GET":
        if pk is not None:
            note=Note.objects.all()
            siri=NoteEditSerializer(note,many=True)
            serializers=NoteSerializer(text,many=False)
            return render(request,'To do list app.html',{'show_edit':serializers.data,'notes':siri.data})





# @unauthenticated_user
def login(request):
        if request.method == "POST":
            username=request.POST["username"]
            password =request.POST["password"]
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                # messages.success(request,"login sucessfull")
                return redirect('/')
            else:
                messages.info(request,"The username or password that you've entered doesn't match any account")
                return redirect("login")

        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")