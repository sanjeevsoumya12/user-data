from django.shortcuts import render 
# from django.contrib.auth.decorators import login_required

# @login_required
def home_view(request):
    return render(request,"home_view.html")


# from django.http import HttpResponse


# name = "justin"
# def home_view(request):
#     HTML_STRING = f"""
#     <h1>Hello {name}</h1>
#     """
#     return HttpResponse(HTML_STRING)
