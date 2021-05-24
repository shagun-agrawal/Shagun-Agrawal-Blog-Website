from django import forms
from django.forms import ModelForm
from .models import *
from django.core import validators
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['firstname','lastname','email','username','password','confirm_password','birthdate']
        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','Placeholder':'Enter Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','Placeholder':'Enter Email'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
            'confirm_password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'ReEnter Password'}),
            'birthdate':forms.TextInput(attrs={'onfocus':"(this.type='date')"}),
        
        }
 
    def clean(self):
        cleaned_data = self.cleaned_data
        firstname =self.cleaned_data.get('firstname')
        lastname=self.cleaned_data.get('lastname')
        email=self.cleaned_data.get('email')
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        birthdate=self.cleaned_data.get('birthdate')
    
        if password != confirm_password:
            self._errors['confirm_password'] = self.error_class([
                "password should be same."
            ])

        if '.' in  lastname:
             self._errors['lastname'] = self.error_class([
               " Last name 'should not be contained '.' ."
            ])
        return self.cleaned_data 
        
class Login(forms.Form):
    email=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))  
class DataForm(forms.ModelForm):
    class Meta:
        fields=['photo','title_name','title']
        model=Data  
       
        widgets={
            'title_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Write Your First Name'}),
            'title':forms.Textarea(attrs={'rows':10,'class':'form-control','Placeholder':'Write Your Blog Here'}),
        }