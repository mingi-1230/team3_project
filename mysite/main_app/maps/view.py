from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  #maps 페이지
  return render(request, "maps/maps.html")
