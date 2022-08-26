from django.contrib import admin

# Register your models here.
from .models import *

# register is a keyword
admin.site.register(worker)# register is a keyword
admin.site.register(jobprovider)
admin.site.register(insuranceagency)
admin.site.register(police)
admin.site.register(additionalinfo1)
admin.site.register(jobs)
admin.site.register(applyjobs)
admin.site.register(complaintjb)
admin.site.register(complaintworker)
admin.site.register(insurance_scheme)
admin.site.register(insurance_scheme1)
admin.site.register(fitnessreport)
admin.site.register(Product)
