from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from . import models
from . import *
from .forms import ProductForm
from .models import Product

from .models import jobs
from .forms import *
from django.core.files.storage import FileSystemStorage


# Create your views here.

# indexpage-home
def index(request):
    return render(request,'index.html')
# about page
def about(request):
    return render(request,'about.html')

 # services page   
def services(request):
    return render(request,'services.html')

  # contact page   
def contact(request):
    return render(request,'contact.html')

 # form page   
def form(request):
    return render(request,'form.html')

def example(request):
    return render(request,'example.html')

# form page   
# def index1_profile(request):
#     return render(request,'index1_profile.html')

 



# dash board  
def workerdash(request):
    return render(request,'workerdash.html')

def jbdash(request):
    return render(request,'jbdash.html')

def index2(request):
    return render(request,'index2.html')


# welcome page example
def home(request):

    id=request.session['id']
    username=request.session['username']
    # email=request.session['name']
    return render(request,'home.html',{'id':id,'username':username})

def home1(request):

    id=request.session['id']
    name=request.session['name']
    # email=request.session['name']
    return render(request,'home1.html',{'id':id,'name':name})

# dashborad
# def index1(request):

#     id=request.session['id']
#     username=request.session['username']
#     # email=request.session['name']
#     return render(request,'index1.html',{'id':id,'username':username})  
# dashboard


# ------worker------

 #  worker register page
def regworker(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        no=request.POST.get('no')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        worker(username=username,email=email,dob=dob,gender=gender,no=no,password=password,password2=password2).save(commit=False)
        worker.status = True
        worker.save()
        return redirect('login')
    else:
        return render(request,'regworker.html')

# -----additional info-----worker dashboard
def worker_profile(request):
    if request.method=="POST":
        place1=request.POST.get('place1')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        wages1=request.POST.get('wages1')
        pan1=request.POST.get('pan1')
        gpay1=request.POST.get('gpay1')
        photo1=request.POST.get('photo1')

        user = worker.objects.get(id=request.session['id'])

        additionalinfo1(worker=user,place1=place1,address1=address1,address2=address2,wages1=wages1,pan1=pan1,gpay1=gpay1,photo1=photo1).save()
        # cr=additionalinfo1.objects.all()
        # cr1=worker.objects.all()
    return render(request,'worker_profile.html')  

  # -----additional info----- worker dashboard   

# def view(request):
#     cr=additionalinfo1.objects.all()
#     return render(request,'worker_profile.html',{'cr':cr})







def jb_addjob(request):
    if request.method=="POST":
        jbtitle=request.POST.get('jbtitle')
        jbplace=request.POST.get('jbplace')
        jbdate=request.POST.get('jbdate')
        jbname=request.POST.get('jbname')
        jbdes=request.POST.get('jbdes')
        jbno=request.POST.get('jbno')
    
        jobs(jbtitle=jbtitle,jbplace=jbplace,jbdate=jbdate,jbdes=jbdes,jbname=jbname,jbno=jbno).save()
    return render(request,'jb_addjob.html')


def add_scheme(request):
    if request.method == "POST":
        policyno = request.POST.get('policyno')
        insurancetype= request.POST.get('insurancetype')
        company = request.POST.get('company')
        timelength = request.POST.get('timelength')
        policyDescription = request.POST.get('policyDescription')
        insuranceamount = request.POST.get('insuranceamount')

        insurance_scheme(policyno=policyno,insurancetype=insurancetype,company=company,timelength=timelength,policyDescription=policyDescription,insuranceamount=insuranceamount).save()
    return render(request,'add_scheme.html')



def jbcomplaint(request):
    if request.method=="POST":
        complaintsub=request.POST.get('complaintsub')
        complaintdes=request.POST.get('complaintdes')
        
        complaintjb(complaintsub=complaintsub,complaintdes=complaintdes).save()
    return render(request,'jbcomplaint.html')


def worker_fitness(request):
    if request.method == 'POST':
        form = fitnessreport(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = fitnessreport()
    return render(request, 'add_scheme.html', {'form': form})







    #  workerlogin page
def login(request):
    return render(request,'login.html')

#  worker login function
def log(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print('email')
        print(email)
        print('password',password)
        # print('password')
        # print(password)

        cr=worker.objects.filter(email=email,password=password)
        if cr:
            user=worker.objects.get(email=email,password=password)
            id=user.id
            print('id',id)
            username=user.username
            email=user.email
            print('email',email)
     

            request.session['id']=id
            
            request.session['email']=email
            request.session['username']=username

            

            return redirect('workerdash')
        else:
            return render(request,'login.html')
    else:
        return render(request,'regworker.html')

# -------worker------

# -------job provider------

 #  job provider register page
def regjobprovider(request):
    if request.method=="POST":
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        no=request.POST.get('no')
        photoid=request.POST.get('photoid')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        jobprovider(user_name=user_name,email=email,dob=dob,gender=gender,photoid=photoid,no=no,password=password,password2=password2).save()
        return redirect('jblogin')
    else:
        return render(request,'regjobprovider.html') 
    # info=None
    # try:
    #     user=worker.objects.get(id=request.session['id'])
    #     info=user.jobprovider
    # except:
    #     pass    
    #     return redirect('jblogin')
    # else:
    # return render(request,'regjobprovider.html',{"info":info})  

#  job provider login page
def jblogin(request):
    return render(request,'jblogin.html')
    
#  job provider login function    
def log1(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
       
      
        print('email')
        print(email)
        print('password',password)
        # print('password')
        # print(password)

        jb=jobprovider.objects.filter(email=email,password=password)
        if jb:
            user=jobprovider.objects.get(email=email,password=password)
            id=user.id
            print('id',id)
            user_name=user.user_name
            email=user.email
            print('email',email)
     
            request.session['id']=id
            
            request.session['email']=email
            request.session['user_name']=user_name

            return redirect('jbdash')
        else:
            return render(request,'jblogin.html')
    else:
        return render(request,'regjobprovider.html')

# -----job provider----


# -----insurance agency----

# insurance agency register page
def reginsurance(request):
    if request.method=="POST":
        regno=request.POST.get('regno')
        name=request.POST.get('name')
        email=request.POST.get('email')
        type1=request.POST.get('type1')
        no=request.POST.get('no')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        insuranceagency(regno=regno,name=name,email=email,type1=type1,no=no,password=password,password2=password2).save()
        return redirect('insurancelogin')
    else:
        return render(request,'reginsurance.html')  
         
 #  insurance agency login page
def insurancelogin(request):
    return render(request,'insurancelogin.html')

#  insurance agency  login function
def log2(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print('email')
        print(email)
        print('password',password)
        # print('password')
        # print(password)

        cr=insuranceagency.objects.filter(email=email,password=password)
        if cr:
            user=insuranceagency.objects.get(email=email,password=password)
            id=user.id
            print('id',id)
            name=user.name
            email=user.email
            print('email',email)
           
           
            

            request.session['id']=id
            
            request.session['email']=email
            request.session['name']=name

            

            return redirect('insurance_dash')
        else:
            return render(request,'insurancelogin.html')
    else:
        return render(request,'reginsurance.html')


def insurance_dash(request):
    return render(request,'insurance_dash.html')

# -----insurance agency----


# -----police----

# # insurance agency register page
# def reginsurance(request):
#     if request.method=="POST":
#         regno=request.POST.get('regno')
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         type1=request.POST.get('type1')
#         no=request.POST.get('no')
#         password=request.POST.get('password')
#         password2=request.POST.get('password2')

#         insuranceagency(regno=regno,name=name,email=email,type1=type1,no=no,password=password,password2=password2).save()
#         return redirect('insurancelogin')
#     else:
#         return render(request,'reginsurance.html')  
         
 # police login page
def policelogin(request):
    return render(request,'policelogin.html')

#  police login function
def log3(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'police_dash.html', {'page': page})
    # else:
    #     return render(request,'index.html')

def police_dash(request):
    return render(request,'police_dash.html')


# ----police----



def worker_viewprof(request):
    cr=additionalinfo1.objects.all()
    return render(request,'worker_viewprof.html',{'cr':cr})



def jb_viewprof(request):
    jb=jobprovider.objects.all()
    # print('user_name',user_name)

    return render(request,'jb_viewprof.html',{'jb':jb})

# def worker_viewprof(request):
#     return render(request,'worker_viewprof.html')


def worker_changepass(request):
    return render(request,'worker_changepass.html')

def worker_viewjob(request):
    job_view = jobs.objects.all() #.filter(status=True)
    return render(request, 'worker_viewjob.html', {'job_view': job_view})


def worker_complaint(request):
    if request.method=="POST":
        complaintsub=request.POST.get('complaintsub')
        complaintdes=request.POST.get('complaintdes')
        
        complaintworker(complaintsub=complaintsub,complaintdes=complaintdes).save()
    return render(request,'worker_complaint.html')

# def jb_viewprof(request):
#     return render(request,'jb_viewprof.html')


def jb_changepass(request):
    return render(request,'jb_changepass.html')

def worker_viewappliedjob(request):
    return render(request,'worker_viewappliedjob.html')


def worker_viewpolicy(request):
    insurance_view = insurance_scheme.objects.all()  # .filter(status=True)
    return render(request,'worker_viewpolicy.html',{'insurance_view': insurance_view})

def worker_viewappliedpolicy(request):
    return render(request,'worker_viewappliedpolicy.html')


def jb_viewaddedjob(request):
    job_view = jobs.objects.all()  # .filter(status=True)
    return render(request,'jb_viewaddedjob.html',{'job_view': job_view})

def logout(request):
    return render(request,'index.html')



def pdf_report_create(request):
    products = jobs.objects.all()

    template_path = 'MWMapp/jb_viewaddedjobs.html'

    context = {'products': products}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def job_apply(request,pk):
    job_new = jobs.objects.filter(id=pk)
    
    context = {"job_new":job_new}    


    return render(request,"worker_viewappliedjob.html",context)

def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        print("hii")
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('workerdash')
    else:
        form = ProductForm()

    context = {
        "form": form
    }

    return render(request, 'worker_fitness.html', context)






