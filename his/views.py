from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from his.models import Hi
from his.forms import HiForm

# Create your views here.
def user_hi(request, user):
    user = get_object_or_404(User, username=user)
    hi_list = Hi.objects.filter(sender=user.id).order_by('-timestamp')
    paginator = Paginator(hi_list, 100)
    page = request.GET.get('page')
    try:
        his = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        his = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        his = paginator.page(paginator.num_pages)
    
    return render(
        request,
        "thehichannel/user.html",
        {
            "his": his
        }
    )

def all_hi(request):
    hi_list = Hi.objects.all().order_by('-timestamp')
    paginator = Paginator(hi_list, 100)
    page = request.GET.get('page')
    try:
        his = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        his = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        his = paginator.page(paginator.num_pages)

    if request.method == "POST":
        request.POST._mutable = True
        request.POST["message"] = "hi"
        request.POST["sender"] = request.user.id
        request.POST._mutable = False
        form = HiForm(request.POST)
        if form.is_valid():
            hi = form.save()
            return redirect("/")
    else:
        form = HiForm()
        return render(
            request,
            "thehichannel/all.html",
            {
                "his": his,
                "form": form
            }
        )

def profile(request):
    pass
