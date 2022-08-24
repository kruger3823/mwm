from django import forms
from .models import *



class registerform(forms.ModelForm):
    class Meta:
        model=worker
        fields=('username','email','dob','gender','no','password','password2')
        widigets={

                  
                   'username':forms.TextInput(attrs={'class' :'form-control'}),
                   'email':forms.TextInput(attrs={'class' :'form-control'}),
                   'dob':forms.TextInput(attrs={'class' :'forms-control'}),
                   'gender':forms.TextInput(attrs={'class' :'forms-control'}),
                   'no':forms.TextInput(attrs={'class' :'form-control'}),
                   'password':forms.TextInput(attrs={'class' :'forms-control'}),
                   'password2':forms.TextInput(attrs={'class' :'forms-control'}),

                #    'place':forms.TextInput(attrs={'class' :'form-control'}),
                #    'address':forms.TextInput(attrs={'class' :'form-control'}),
                #    'address1':forms.TextInput(attrs={'class' :'forms-control'}),
                #    'wages':forms.TextInput(attrs={'class' :'forms-control'}),
                #    'pan':forms.TextInput(attrs={'class' :'form-control'}),
                #    'gpay':forms.TextInput(attrs={'class' :'forms-control'}),
                #    'photo':forms.TextInput(attrs={'class' :'forms-control'}),
        }   

class addinfo(forms.ModelForm):
    class Meta:
        model=additionalinfo1
        fields=('place1','address1','address2','wages1','pan1','gpay1','photo1')
        widigets={


                   'place1':forms.TextInput(attrs={'class' :'form-control'}),
                   'address1':forms.TextInput(attrs={'class' :'form-control'}),
                   'address2':forms.TextInput(attrs={'class' :'forms-control'}),
                   'wages1':forms.TextInput(attrs={'class' :'forms-control'}),
                   'pan1':forms.TextInput(attrs={'class' :'form-control'}),
                   'gpay1':forms.TextInput(attrs={'class' :'forms-control'}),
                   'photo1':forms.TextInput(attrs={'class' :'forms-control'}),
        }   

class addjob(forms.ModelForm):
    class Meta:
        model=jobs
        fields=('jbtitle','jbplace','jbdate','jbname','jbdes','jbno')
        widigets={


                   'jbtitle':forms.TextInput(attrs={'class' :'form-control'}),
                   'jbplace':forms.TextInput(attrs={'class' :'form-control'}),
                   'jbdate':forms.TextInput(attrs={'class' :'forms-control'}),
                   'jbname':forms.TextInput(attrs={'class' :'forms-control'}),
                   'jbdes':forms.TextInput(attrs={'class' :'form-control'}),
                   'jbno':forms.TextInput(attrs={'class' :'forms-control'}),
                  
        }   


class addcomplaint(forms.ModelForm):
    class Meta:
        model=complaintjb
        fields=('complaintsub','complaintdes')
        widigets={


                   'complaintsub':forms.TextInput(attrs={'class' :'form-control'}),
                   'complaintdes':forms.TextInput(attrs={'class' :'form-control'}),
                  
                  
        }   


class addcomplaint1(forms.ModelForm):
    class Meta:
        model=complaintworker
        fields=('complaintsub','complaintdes')
        widigets={


                   'complaintsub':forms.TextInput(attrs={'class' :'form-control'}),
                   'complaintdes':forms.TextInput(attrs={'class' :'form-control'}),
                  
                  
        }   










class registerform(forms.ModelForm):
    class Meta:
        model=jobprovider
        fields=('user_name','email','dob','gender','no','photoid','password','password2')
        widigets={

                  
                   'user_name':forms.TextInput(attrs={'class' :'form-control'}),
                   'email':forms.TextInput(attrs={'class' :'form-control'}),
                   'dob':forms.TextInput(attrs={'class' :'forms-control'}),
                   'gender':forms.TextInput(attrs={'class' :'forms-control'}),
                   'no':forms.TextInput(attrs={'class' :'form-control'}),
                   'photoid':forms.FileField(),
                   'password':forms.TextInput(attrs={'class' :'forms-control'}),
                   'password2':forms.TextInput(attrs={'class' :'forms-control'}),
        }   


class registerjb(forms.ModelForm):
    class Meta:
        model=insuranceagency
        fields=('regno','name','email','type1','no','password','password2')
        widigets={

                  
                   'regno':forms.TextInput(attrs={'class' :'form-control'}),
                   'name':forms.TextInput(attrs={'class' :'form-control'}),
                   'email':forms.TextInput(attrs={'class' :'forms-control'}),
                   'type1':forms.TextInput(attrs={'class' :'forms-control'}),
                   'no':forms.TextInput(attrs={'class' :'form-control'}),
                   'password':forms.TextInput(attrs={'class' :'forms-control'}),
                   'password2':forms.TextInput(attrs={'class' :'forms-control'}),
        }   


class registerjb(forms.ModelForm):
    class Meta:
        model=police
        fields=('email','password')
        widigets={

                  
                #    'policeid':forms.TextInput(attrs={'class' :'form-control'}),
                #    'name':forms.TextInput(attrs={'class' :'form-control'}),
                #    'station':forms.TextInput(attrs={'class' :'forms-control'}),
                #    'no':forms.TextInput(attrs={'class' :'forms-control'}),
                   'email':forms.TextInput(attrs={'class' :'forms-control'}),
                   'password':forms.TextInput(attrs={'class' :'forms-control'}),
                   
        }   


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['eye', 'adhar', 'fitness', 'yesno']
        widgets = {
            'eye': forms.FileInput(attrs={'class': 'form-control'}),
            'adhar': forms.FileInput(attrs={'class': 'form-control'}),
            'fitness': forms.FileInput(attrs={'class': 'form-control'}),
            'yesno': forms.TextInput(attrs={'class': 'form-control'}),
        }
