from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Msg

# Create your views here.

def create(request):
    print("request =" , request.method)
    if request.method =="GET":
        print("We are inside GET method")
        return render(request,"create.html")
    else:
        print("We are inside POST method.")
        nm=request.POST["name"]
        ph=request.POST["phone"]
        em=request.POST["email"]
        msg=request.POST["message"]
        # print ( nm )
        # print ( ph )
        # print ( em )
        # print ( msg )
        m = Msg.objects.create(name=nm, email=em , mobile=ph, message=msg)

        print(m)

        # return HttpResponse("data stored successfully")
        return redirect('/user-details')




def udl(request):
    user_details = Msg.objects.all()
    return render(request, 'udl.html', {'user_details': user_details})

def delete(request, rid):
    # record = get_object_or_404(Msg, id=rid)
    # Perform the deletion
    # record.delete()
    # return HttpResponse(f"Deleting record with id: {rid}")
    print("delete id=", rid)
    dl = Msg.objects.filter(id=rid).delete()
    return redirect ("/user-details")

def edit(request, rid):
    if request.method == "GET":

        m=Msg.objects.filter(id=rid)
        context={}
        context["data"]=m
        return render(request,"edit.html",context)
    else:
        nm=request.POST["name"]
        ph=request.POST["phone"]
        em=request.POST["email"]
        msg=request.POST["message"]
        
        m = Msg.objects.filter(id=rid).update(name=nm, email=em , mobile=ph, message=msg)
        
        print(m)

        return redirect("/user-details")
    
