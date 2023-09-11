

# Create your views here.
from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect
import time


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
   
    
   
def login(request):
    if request.method != "POST" :
       return render(request, 'member/loginForm.html')   
   
    else :
      id1=request.POST["id"] 
      pass1=request.POST["pass"]
      try :
          #입력된 id값으로 Member 객체에서 조회
          member = Member.objects.get(id=id1) #select 문장 실행
      except :  #db에 아이디 정보가 없을 때
          context = {"msg":"아이디를 확인하세요.","url":"/member/login/"}
          return render(request,"alert.html",context)
      else :  #정상적인 경우. 아이디 정보가 조회된 경우
          #member.pass1 : db에 등록된 비밀번호
          #pass1 : 입력된 비밀번호
          if member.pass1 == pass1 :  #로그인 정상
             request.session["id"] = id1  #session 객체에 login 등록.
             time.sleep(1)
             print("2:",request.session.session_key)
             return HttpResponseRedirect("/member/index/")
          else :  #비밀번호 오류
              context = {"msg":"비밀번호가 틀립니다.","url":"/member/login/"}
              return render(request,"alert.html",context)
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
   
    
   
    
   
    
   