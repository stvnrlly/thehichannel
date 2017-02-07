from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from his.models import Hi
from his.forms import HiForm

# Create your views here.
def user_hi(request, user):
    user = get_object_or_404(User, username=user)
    his = Hi.objects.filter(sender=user.id).order_by('-timestamp')
    return render(
        request,
        "thehichannel/user.html",
        {
            "his": his
        }
    )

def all_hi(request):
    his = Hi.objects.all().order_by('-timestamp')
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
