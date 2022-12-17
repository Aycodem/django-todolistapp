from django.shortcuts import render,redirect
from .models import Note
from .serializer import NoteSerializer
from django.contrib import messages
# Create your views here.

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
        serializer=NoteSerializer(text,many=True)
        return render(request,'To do list app.html',{'notes':serializer.data})
    return render(request,'To do list app.html')


def delete(request,pk):
    textnote=Note.objects.get(id=pk)
    textnote.delete()
    return redirect('/')

def Update(request,pk):
    pass

   