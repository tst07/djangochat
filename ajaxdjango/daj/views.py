from django.shortcuts import render
from .models import Chat
# Create your views here.

def welcome(request):
    if request.method == "POST":
        data = request.POST['msg']
        usr  = request.POST['user']
        u = Chat(author = usr ,message = data)
        u.save()
        
        msgs = Chat.objects.all()
        return render(request,'daj/home.html',{'msgs' : msgs})
    else:
        msgs = Chat.objects.all()
        return render(request,'daj/home.html', {'msgs' : msgs})
