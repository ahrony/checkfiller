from datetime import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import RequestContext
from .forms import *


from check.models import *
# from check.forms import *
# Create your views here.





def index(request):
	return render(request, 'check/index.html', {})

def add_new(request):

    if request.method == 'POST':

        form = CheckDetailsForm(request.POST)

        if form.is_valid():
        	form.save(commit=True)
        	return redirect('/index/')
        else:
        	print form.errors

    else:
        form = CheckDetailsForm()

    return render(request,'check/new.html', { 'form':form })

def archive(request):
    info = Checkdetails.objects.all()
    context_dict = {"info": info}
    return render(request, 'check/archive.html', context_dict)


def contact(request):
    return render(request, 'check/contact.html', {})

def test(request):
    return render(request, 'check/test.html', {})



