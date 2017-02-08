import os
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def challenge(request, id):
    code = os.environ.get("LETS_ENCRYPT_CHALLENGE")
    return HttpResponse("{0}.{1}".format(id, code))
