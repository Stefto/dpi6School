from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    with open('DPIFrontEnd\html\overview.html') as cf:
        return HttpResponse(cf.read())


def getlistofhdds(request):
    return HttpResponse('test')


def getsinglehdd(request):
    return HttpResponse('single')
