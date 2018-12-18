from  django import forms
from .models import *
class student(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=100)
    emailid=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Adress'}),required=True,max_length=100)
    phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone-Number'}),required=True,max_length=100)
    address1=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Address'}),required=True,max_length=1000)
    education=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Education'}),required=True,max_length=100)
    url = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control','placeholder':'Education'}), required=False)
    paddress=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Permanent-Address'}),required=True,max_length=1000)
    hacker=forms.CharField(widget=forms.URLInput(attrs={'class':'form-control','placeholder':'HackerRank link'}),required=False,max_length=1000)
    linkdin=forms.CharField(widget=forms.URLInput(attrs={'class':'form-control','placeholder':'Linkedin profile link'}),required=False,max_length=10000)
    git=forms.CharField(widget=forms.URLInput(attrs={'class':'form-control','placeholder':'GitHub Profile link'}),required=False,max_length=10000)
    blog=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Write something about you'}),required=True,max_length=10000)

    class Meta():
         model=login1
         fields=['name','emailid','phone','address1','education','url','paddress','hacker','linkdin','git','blog']


