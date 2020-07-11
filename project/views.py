# i have creared this

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {"name":"raman dahiya","place":"shamli"}
    return  render(request,'index.html')
