from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from his.models import Hi
from his.forms import HiForm
from his.serializers import HiSerializer, PostSerializer

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

@login_required
def profile(request):
    return render(request, "thehichannel/profile.html")

@login_required
def refresh_token(request):
    token = Token.objects.get_or_create(user=request.user)[0]
    token.delete()
    Token.objects.create(user=request.user)
    return redirect("/account/profile/")

def api_docs(request):
    return render(request, "thehichannel/api_docs.html")

@api_view(['GET'])
def api_user_hi(request, user):
    if request.method == "GET":
        user = get_object_or_404(User, username=user)
        hi_list = Hi.objects.filter(sender=user.id).order_by('-timestamp')
        serializer = HiSerializer(hi_list, many=True)

        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_post_hi(request):
    if request.method == "POST":
        data = request.data
        data['sender'] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"hi": "hi"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
