from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  #dashboard 페이지
  return render(request, "dashboard/dashboard.html")
