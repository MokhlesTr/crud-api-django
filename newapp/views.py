from django.shortcuts import redirect , render,get_object_or_404
from .models import Member

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Member
import json


def index (request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['first']
    z=request.POST['first']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def delete(request,id):
        mem=Member.objects.get(id=id)
        mem.delete()
        return redirect("/")

@csrf_exempt
def api_members(request, id=None):
    if request.method == 'GET':
        if id:
            member = get_object_or_404(Member, id=id)
            return JsonResponse(member.serialize())
        else:
            members = Member.objects.all()
            serialized_members = [member.serialize() for member in members]
            return JsonResponse(serialized_members, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        firstname = data['firstname']
        lastname = data['lastname']
        country = data['country']
        mem = Member(firstname=firstname, lastname=lastname, country=country)
        mem.save()
        return JsonResponse(mem.serialize(), status=201)
    
    elif request.method == 'PUT':
        member = get_object_or_404(Member, id=id)  # Use the ID from the URL
        data = json.loads(request.body)
        firstname = data.get('firstname', member.firstname)
        lastname = data.get('lastname', member.lastname)
        country = data.get('country', member.country)
        
        member.firstname = firstname
        member.lastname = lastname
        member.country = country
        member.save()
        
        return JsonResponse(member.serialize(), status=200)
    
    elif request.method == 'DELETE':
        member = get_object_or_404(Member, id=id)
        member.delete()
        return JsonResponse({'message': 'Member deleted'}, status=204)



   