from django.shortcuts import render
from django.http import HttpResponse


def sey_hello(request):
    return render(request, "hello.html", {"name": "Lislain"})
