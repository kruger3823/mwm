from django.urls import path
from.import views
from django.conf.urls.static import static,settings




urlpatterns=[
    path('',views.index,name="index"),
    # path('index/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact"),


# ----worker-reg---
    path('regworker/',views.regworker,name="regworker"),
    path('login/',views.login,name="login"),
    path('log/',views.log,name="log"),
# ----worker-reg---

# ----jobprovider-reg---

    path('regjobprovider/',views.regjobprovider,name="regjobprovider"),
    path('jblogin/',views.jblogin,name="jblogin"),
    path('log1/',views.log1,name="log1"),
  #  path('job_view/',views.jobs,name="job_view"),
# ----jobprovider-reg---

# ----insurance-reg---
    path('reginsurance/',views.reginsurance,name="reginsurance"),
    path('insurancelogin/',views.insurancelogin,name="insurancelogin"),
    path('log2/',views.log2,name="log2"),
# ----insurance-reg---

# ----police-reg---

    path('policelogin/',views.policelogin,name="policelogin"),
    path('log3/',views.log3,name="log3"),
# ----police-reg---



     path('home/',views.home,name="home"),
     path('home1/',views.home1,name="home1"),

# dashbord
     path('workerdash/',views.workerdash,name="workerdash"),
     path('index2/',views.index2,name="index2"),
# dashbord
     path('form/',views.form,name="form"),
     path('worker_profile/',views.worker_profile,name="worker_profile"),
     path('jbdash/',views.jbdash,name="jbdash"),

     path('jb_addjob/',views.jb_addjob,name="jb_addjob"),
     path('example/',views.example,name="example"),
     path('jbcomplaint/',views.jbcomplaint,name="jbcomplaint"),
     #path('worker_fitness/',views.worker_fitness,name="worker_fitness"),
    #  path('view/',views.view,name="view"),
     path('worker_viewprof/',views.worker_viewprof,name="worker_viewprof"),
     path('worker_changepass/',views.worker_changepass,name="worker_changepass"),
     path('worker_viewjob/',views.worker_viewjob,name="worker_viewjob"),
    path('worker_fitness/', views.addProduct, name="worker_fitness"),
    path('worker_complaint/',views.worker_complaint,name="worker_complaint"),
     path('jb_viewprof/',views.jb_viewprof,name="jb_viewprof"),
     path('jb_changepass/',views.jb_changepass,name="jb_changepass"),
     path('insurance_dash/',views.insurance_dash,name="insurance_dash"),

     path('police_dash/',views.police_dash,name="police_dash"),
     path('worker_viewappliedjob/',views.worker_viewappliedjob,name="worker_viewappliedjob"),
     path('worker_viewpolicy/',views.worker_viewpolicy,name="worker_viewpolicy"),
     path('worker_viewappliedpolicy/',views.worker_viewappliedpolicy,name="worker_viewappliedpolicy"),
     path('jb_viewaddedjob/',views.jb_viewaddedjob,name="jb_viewaddedjob"),
     path('add_scheme/',views.add_scheme,name="add_scheme"),
     path('logout/', views.logout, name="logout"),

     path('job-apply/<int:pk>/', views.job_apply, name="job-apply"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
