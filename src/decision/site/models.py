from django.db import models
from django.forms import ModelForm
from django import forms

class group(models.Model):    
    group_id = models.IntegerField(primary_key=True)
    
    users = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.group_id.__str__()
    
class idea(models.Model):
    IDEA_STATUS=(('A','Agreed'),('D','Disagree'),('C','Counter'),('P','Pending'))
    IDEA_STATUS_CHOICE=(('A','Agreed'),('D','Disagree'),('C','Counter'))
    
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1, choices=IDEA_STATUS)
    description = models.CharField(max_length=99)
    statement = models.CharField(max_length=99)
    opinion = models.CharField(max_length=99, blank=True)
    
    def __str__(self):
        return self.id.__str__()
    
class ideaResponseForm(ModelForm):
    
    status = forms.ChoiceField(choices=idea.IDEA_STATUS_CHOICE, widget=forms.RadioSelect())
    
    class Meta:
        model = idea
        fields = ['status', 'opinion', ]