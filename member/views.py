

# Create your views here.
from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect
from django.contrib import auth
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
          
            
def info(request, id):
   member = Member.objects.get(id=id)
   return render(request,"member/memberInfo.html",{"mem":member})

def update(request, id):
    member = Member.objects.get(id=id)
    if request.method != "POST" :
        return render(request,"member/memberUpdateForm.html",{"mem":member})
    else :
       #비밀번호 검증. 
       #비밀번호 오류시 비밀번호 오류 메세지, update.html 페이지 출력
       #member.pass1 : db에 등록된 비밀번호
       # request.POST["pass"] : 입력된 비밀번호
       if request.POST["pass"] == member.pass1:
          member = Member(id=id,\
                    pass1=request.POST["pass"],\
                    name=request.POST["name"],
                    gender=request.POST["gender"],
                    tel=request.POST["tel"],
                    email=request.POST["email"],
                    picture=request.POST["picture"]) 
          #id값존재:update, id값없으면 insert    
          member.save() #update 문장 실행.
          return HttpResponseRedirect("/member/info/"+id+"/")
       else :
          context = {"msg":"비밀번호 오류입니다.",\
                   "url":"/member/update/"+id+"/"}
          return render(request,"alert.html",context)
    
   
def delete(request, id) :
    if request.method != "POST" :
        return render(request,"member/memberDeleteForm.html",{"id":id})
    else :
        login = request.session["id"]
        member = Member.objects.get(id=login)
        if member.pass1 == request.POST["pass"] : #비밀번호 일치 
           member.delete()
           auth.logout(request)
           context={"msg":"탈퇴완료","url":"/member/login/"}
           return render(request,"alert.html",context)
        else :
           context={"msg":"비밀번호 오류",\
                  "url":"/member/delete/"+id+"/"}
           return render(request,"alert.html",context) 
    
   
def logout(request) :    
   auth.logout(request)
   return HttpResponseRedirect("/member/login/")
    
   
def list(request) :
   try :
       login = request.session["id"]
   except :
       context={"msg":"로그인 하세요","url":"/member/login/"}
       return render(request,"alert.html",context)
   else :
       if login != "admin" :
          context={"msg":"관리자만 가능합니다","url":"/member/index/"}
          return render(request,"alert.html",context)
       #mlist 요소: Member 객체 
       mlist = Member.objects.all() #모든데이터 리턴
       return render(request,"member/memberList.html",{"mlist":mlist})    
   
   
def passchg(request) :  
    login=request.session["id"]
    if request.method != "POST" :
       return render(request,"member/memberPassForm.html")   
    else :  
       member = Member.objects.get(id=login)   
       if member.pass1 == request.POST["pass"] :  #비밀번호 비교
          member.pass1 = request.POST["chgpass1"] #변경할 비밀번호로 비밀번호값 수정
          member.save() #수정
          context={"msg":"비밀번호 수정 완료","url":"/member/info/"+login+"/"}
          return render(request,"alert.html",context)        
       else :  #비밀번호 오류
          context={"msg":"비밀번호 오류",  "url":"/member/passchg/"}
          return render(request,"alert.html",context)
    
   
    
   
    
   