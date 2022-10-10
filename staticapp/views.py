from django.shortcuts import render
from django.http import HttpResponse
from staticapp.models import Denination
# from django.template import loader

from django.conf import settings
from django.core.mail import send_mail




def home(request):

    # hi = Denination()
    # hi.title="Trichy"
    # hi.price=249
    # hi.content="Trichy is a best place for op"
    # hi.img="destination_1.jpg"
    # hi.offer=True

    # thur = Denination()
    # thur.price=199
    # thur.img="destination_3.jpg"
    # thur.title="Thuraiyur"
    # thur.content="Thuraiyur child river"
    # thur.offer=True

    # mu = Denination()
    # mu.price=199
    # mu.title="Musiri"
    # mu.img="destination_2.jpg"
    # mu.content="AAGAC in Musiri"
    # mu.offer=False

    # detail = [hi,thur,mu]

    detail =  Denination.objects.all()
    
    return render(request,'index.html',{'hi':detail})


    
   


