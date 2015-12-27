from django.shortcuts import render, get_object_or_404
import os
from decision.site.models import *
from django.http import HttpResponseRedirect
import logging

def master(request):
    
    context = {'ideas' : idea.objects.all()}
    return render(request, 'master.html', context)


def ideaInfo(request, ideaId):
    if request.method == 'POST': # If the form has been submitted...
        form = ideaResponseForm(request.POST) # A form bound to the POST data
        
        if form.is_valid():
            ideaInfo=get_object_or_404(idea, id=ideaId)
            ideaInfo.status=form.cleaned_data['status']
            
            form_opinion=form.cleaned_data['opinion']
            if form_opinion != '':
                ideaInfo.opinion=form_opinion
                
            ideaInfo.save()
            return HttpResponseRedirect('/')
        
        else:
            print("bad form")
            return HttpResponseRedirect('/idea/'+ideaId)    
        
    form = ideaResponseForm()
    ideaInfo=get_object_or_404(idea ,id=ideaId)
    context={
             'id' : ideaInfo.id
             , 'description' : ideaInfo.description
             , 'statement' : ideaInfo.statement
             , 'opinion' : ideaInfo.opinion
             , 'status' : ideaInfo.status
             , 'form': form
             }
    
    return render(request, 'idea.html', context)    