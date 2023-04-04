from django.shortcuts import render

import phonenumbers
from phonenumbers import timezone,geocoder,carrier



def index(request):
    return render(request,"index.html")




def get(request):
    number=request.POST['num']
    phone=phonenumbers.parse(number,'ch')
    car=carrier.name_for_number(phone,"en")
    reg=geocoder.description_for_number(phone,'en')
    
    return render(request,"index.html",{'sim':car,'location':reg})
    