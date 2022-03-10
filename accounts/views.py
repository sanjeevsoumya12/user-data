from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .form import  CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    # print(request.method)
    print(request.user)
    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        # print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is  None:
            # context = {"error": "Invalid username or password"}
            # return render(request,"accounts/login.html",context)
            messages.info(request, "Invalid username or password")
        else:
            login(request,user)
            return redirect("/upload/")
    return render(request,"accounts/login.html",{})

def logout_view(request):
    # if request.method == "POST":
        logout(request)
        return redirect("/")
    # return render(request,"accounts/logout.html",{})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        form =  CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,"Account was created for" + user)
            return redirect("/")
        context = {
            "form": form
        }
    return render(request,"accounts/register.html",context)