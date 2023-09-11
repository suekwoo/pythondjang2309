

# Create your views here.
from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'member/index.html')  #templates



def join(request):
    if request.method != "POST" :
       return render(request, 'member/joinForm.html')  #templates/member/joinForm.html
    else :
       member = Member(id=request.POST["id"],\
                    pass1=request.POST["pass"],\
                    name=request.POST["name"],
                    gender=request.POST["gender"],
                    tel=request.POST["tel"],
                    email=request.POST["email"],
                    picture=request.POST["picture"]) 
       member.save() #insert, update(같은 id)  문장 실행.
       return HttpResponseRedirect("/member/login/")
   
    
   
    
   
    
   
    
   
    
   