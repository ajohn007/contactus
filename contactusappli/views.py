from django.shortcuts import render, redirect
from . models import Contact
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import ContactModelForm

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from contactusappli.models import Contact
from contactusappli.serializers import ContactusSerializer
from rest_framework.decorators import api_view

# Create your views here.

def contact(request):
    all_contact=Contact.objects.all()
    template='contactusappli/index.html'
    return render(request,template,{'contactsall':all_contact})

def create_user(request):
    
    if request.method=='POST':
        name= request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        subject=request.POST['subject']

        Contact.objects.create(

            name=name,
            email=email,
            number=number,
            subject=subject

        )
        return HttpResponse("Sucess")


@api_view(['GET','POST'])

def contactDetails(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            contacts = contacts.filter(name_icontains = name)
        contactSerial = ContactusSerializer(contacts, many= True)
        return JsonResponse(contactSerial.data, safe = False)
    
    elif request.method == 'POST':
        contactData = JSONParser().parse(request)
        contactSerial = ContactusSerializer(data = contactData)
        if contactSerial.is_valid():
            contactSerial.save()
            return JsonResponse(contactSerial.data, status = status.HTTP_201_CREATED)
        return JsonResponse(contactSerial.errors, status = status.HTTP_400_BAD_REQUEST)

