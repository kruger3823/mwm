from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class worker(models.Model):
    username=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    dob=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=200,null=True) 
    no=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True) 
    password2=models.CharField(max_length=200,null=True)

    # place1=models.CharField(max_length=200,null=True)
    # address1=models.CharField(max_length=200,null=True)
    # address11=models.CharField(max_length=200,null=True)
    # wages1=models.CharField(max_length=200,null=True) 
    # pan1=models.CharField(max_length=200,null=True)
    # gpay1=models.CharField(max_length=200,null=True) 
    # photo1=models.CharField(max_length=200,null=True)

class fitnessreport(models.Model):
    image= models.ImageField(null=True,blank=True,upload_to="media/")

class jobprovider(models.Model):
    user_name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    dob=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=200,null=True) 
    no=models.CharField(max_length=200,null=True)
    photoid=models.FileField(null=False,blank=False)
    password=models.CharField(max_length=200,null=True) 
    password2=models.CharField(max_length=200,null=True)

class insuranceagency(models.Model):
    regno=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    type1=models.CharField(max_length=200,null=True) 
    no=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True) 
    password2=models.CharField(max_length=200,null=True)

class insurance_scheme(models.Model):
    policyno= models.CharField(max_length=200, null=True)
    insurancetype= models.CharField(max_length=200, null=True)
    company= models.CharField(max_length=200, null=True)
    policyDescription= models.CharField(max_length=200, null=True)
    timelength= models.CharField(max_length=200, null=True)
    insuranceamount= models.CharField(max_length=200, null=True)


class police(models.Model):
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True) 

class additionalinfo1(models.Model):
    worker = models.ForeignKey(worker, on_delete=models.CASCADE)
    place1=models.CharField(max_length=200,null=True)
    address1=models.CharField(max_length=200,null=True)
    address2=models.CharField(max_length=200,null=True)
    wages1=models.CharField(max_length=200,null=True) 
    pan1=models.CharField(max_length=200,null=True)
    gpay1=models.CharField(max_length=200,null=True) 
    photo1=models.CharField(max_length=200,null=True)


class jobs(models.Model):
    jbtitle=models.CharField(max_length=200,null=True)
    jbplace=models.CharField(max_length=200,null=True)
    jbdate=models.CharField(max_length=200,null=True)
    jbname=models.CharField(max_length=200,null=True) 
    jbdes=models.CharField(max_length=200,null=True)
    jbno=models.CharField(max_length=200,null=True) 
    jbstatus=models.BooleanField()

class complaintjb(models.Model):
    complaintsub=models.CharField(max_length=200,null=True)
    complaintdes=models.CharField(max_length=200,null=True)



class complaintworker(models.Model):
    complaintsub=models.CharField(max_length=200,null=True)
    complaintdes=models.CharField(max_length=200,null=True)
   

# class fitness(models.Model):
#     complaintsub=models.CharField(max_length=200,null=True)
#     complaintdes=models.CharField(max_length=200,null=True)

class Product(models.Model):
    eye = models.ImageField(null=False, blank=False)
    adhar = models.ImageField(null=False, blank=False)
    fitness = models.ImageField(null=False, blank=False)
    yesno = models.CharField(max_length=200, null=False, blank=False)



    