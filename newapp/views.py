from django.shortcuts import render
from .models import Member
def index (request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})