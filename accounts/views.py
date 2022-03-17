from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import CustomUserCreationForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.http import HttpResponse  
# from django.shortcuts import render, redirect  
# from django.contrib.auth import login, authenticate  
# # from .forms import SignupForm  
# from django.contrib.sites.shortcuts import get_current_site  
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.template.loader import render_to_string  
# # from .tokens import account_activation_token  
# from django.contrib.auth.models import User  
# from django.core.mail import EmailMessage  
# from accounts.token import TokenGenerator


# Create your views here.
def login_view(request):
    # print(request.method)
    if request.user.is_authenticated:
        return redirect("/datas/upload/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            # context = {"error": "Invalid username or password"}
            # return render(request,"accounts/login.html",context)
            messages.info(request, "Invalid username or password")
        else:
            login(request, user)
            return redirect("/datas/upload/")
    return render(request, "accounts/login.html", {})

def logout_view(request):
    # if request.method == "POST":
    if not request.user.is_authenticated:
        return redirect("/")
    logout(request)
    return redirect("/")
    # return render(request,"accounts/logout.html",{})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/datas/upload/")
    else:
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            #for flash messgaes
            # user = form.cleaned_data.get("username")
            # messages.success(request, "Account was created for" + user)
            return redirect("/")
        context = {
            "form": form
        }
    return render(request, "accounts/register.html", context)
    # if request.method == 'POST':  
    #     form =  CustomUserCreationForm(request.POST)  
    #     if form.is_valid():  
    #             # save form in the memory not in database  
    #             user = form.save(commit=False)  
    #             user.is_active = False  
    #             user.save()  
    #             # to get the domain of the current site  
    #             current_site = get_current_site(request)  
    #             mail_subject = 'Activation link has been sent to your email id' 
    #             message = render_to_string('accounts/acc_active_email.html', {  
    #                 'user': user,  
    #                 'domain': current_site.domain,  
    #                 'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),  
    #                 'token':TokenGenerator.make_token(user),  
    #             })  
    #             to_email = form.cleaned_data.get('email')  
    #             email = EmailMessage(  
    #                         mail_subject, message, to=[to_email]  
    #             )  
    #             email.send()  
    #             return   render(request, 'accounts/register.html')  
    #     else:  
    #         form =  CustomUserCreationForm()  
    #     return render(request, 'accounts/register.html', {'form': form})  

def home_view(request):
    return render(request,"home_view.html")