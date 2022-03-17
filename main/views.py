from multiprocessing import context
from posixpath import split
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .forms import DataForm
from .models import Datas
# for search
from django.db.models import Q
from functools import reduce
# for pagination
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def data_search_view(request, id=None):
    query_dict = request.GET
    query = query_dict.get("q")
    print(query)
    data_obj = None
    if query is not None:
      data_obj = Datas.objects.filter(description__icontains=query)
    else:
        data_obj = None
    context = {
        "object": data_obj
    }
    return render(request, "search.html", context=context)


def upload_data(request):
    # print(request.GET)
    # query_dict = request.GET
    # query = query_dict.get("q")
    # if query :
    #     data_obj = Datas.objects.filter(description=query)

    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            print(request.user)
            instance.uploder = request.user
            instance.save()
            return redirect("/datas/upload/")
    else:
        form = DataForm()
    data_list = Datas.objects.filter(uploder=request.user)
    page = request.GET.get('page', 1)  # page number is default set as 1

    paginator = Paginator(data_list, 3)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    # return render(request, 'upload_data.html', { 'datas': page_obj })
    return render(request, "upload_data.html", {
        "form": form,
        'datas': datas
    })


# class UserListView(ListView):
#     model = Datas
#     template_name = 'upload_data.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'users'  # Default: object_list
#     paginate_by = 2
#     queryset = Datas.objects.all()

# @login_required(login_url="/")
# def upload(request):
#     context = {}
#     if not request.user.is_authenticated:
#         return redirect("/")
#     if request.method == 'POST':
#         uploaded_file = request.FILES["document"]
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context["url"] = fs.url(name)
#     return render(request, "upload.html", context)


# def data_list(request):
#     datas = Datas.objects.all()
#     return render(request, "upload_data.html",{
#         "datas": datas
#     })
