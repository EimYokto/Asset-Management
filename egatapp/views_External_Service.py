from django.shortcuts import render , redirect
from egatapp.models import *
from tablib import Dataset
from egatapp.resources import *
# Create your pages.
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.contrib.auth.models import User

# External service

@permission_required("egatapp.view_external_service", login_url="/login")
def External_service_show(request):
    External_services = External_service.objects.all()
    return render(request,'Asset_Management/External service/DataTable.html',{'External_services':External_services} )

@permission_required("egatapp.add_external_service", login_url="/login")
def External_service_insert(request):
    if request.method == "POST":
        Asset_Code = None
        Service_Detail = request.POST['Service_Detail']
        Vendor_Name = request.POST['Vendor_Name']
        Address = request.POST['Address']
        Product = request.POST['Product']
        Confidential = request.POST['Confidential']
        Integrity = request.POST['Integrity']
        Availability = request.POST['Availability']
        Service_Owner = request.POST['Service_Owner']
        Contract_Number = request.POST['Contract_Number']
        Contract_Start_Date = request.POST['Contract_Start_Date']
        Contract_End_Date = request.POST['Contract_End_Date']
        Repository = request.POST['Repository']
        Storage_Media= request.POST['Storage_Media']
        Phone = request.POST['Phone']

        last_External_service = External_service.objects.count()
        last_pk = 0
        if last_External_service:
            last_pk = last_External_service
            
        Asset_Code_Historys = "D403021-" + "ESER-" + str(last_pk+1).zfill(5)

        USER = request.user
        Database = "External_service"
        Record = Asset_Code_Historys
        ACTION = "Add"

        data = External_service(Asset_Code=Asset_Code, Service_Detail=Service_Detail, Vendor_Name=Vendor_Name, 
        Address=Address,Product=Product,Confidential= Confidential,Integrity=Integrity,Availability=Availability,
        Service_Owner=Service_Owner,Contract_Number=Contract_Number,Contract_Start_Date=Contract_Start_Date,
        Contract_End_Date=Contract_End_Date,Repository=Repository,Storage_Media=Storage_Media,Phone=Phone)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('External_service_show')
    else:
        return render(request, 'Asset_Management/External service/DataTable.html')

@permission_required("egatapp.change_external_service", login_url="/login")
def External_service_edit(request,Asset_Code):
    if request.method == "POST":
        Asset_Code = request.POST.get('Asset_Code')
        Service_Detail = request.POST.get('Service_Detail')
        Vendor_Name = request.POST.get('Vendor_Name')
        Address = request.POST.get('Address')
        Product = request.POST.get('Product')
        Confidential = request.POST.get('Confidential')
        Integrity = request.POST.get('Integrity')
        Availability = request.POST.get('Availability')
        Service_Owner = request.POST.get('Service_Owner')
        Contract_Number = request.POST.get('Contract_Number')
        Contract_Start_Date = request.POST.get('Contract_Start_Date')
        Contract_End_Date = request.POST.get('Contract_End_Date')
        Repository = request.POST.get('Repository')
        Storage_Media= request.POST.get('Storage_Media')
        Phone= request.POST.get('Phone')

        USER = request.user
        Database = "External_service"
        Record =  request.POST.get('Asset_Code')
        ACTION = "Edit"

        data = External_service(Asset_Code=Asset_Code, Service_Detail=Service_Detail, Vendor_Name=Vendor_Name, 
        Address=Address,Product=Product,Confidential= Confidential,Integrity=Integrity,Availability=Availability,
        Service_Owner=Service_Owner,Contract_Number=Contract_Number,Contract_Start_Date=Contract_Start_Date,
        Contract_End_Date=Contract_End_Date,Repository=Repository,Storage_Media=Storage_Media,Phone=Phone)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('External_service_show')
    return redirect(request,'Asset_Management/External service/DataTable.html')

@permission_required("egatapp.delete_external_service", login_url="/login")
def External_service_delete(request,Asset_Code):
    External_services = External_service.objects.filter(Asset_Code = Asset_Code)

    USER = request.user
    Database = "External_service"
    Record = Asset_Code
    ACTION = "Delete"

    
    Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
    Historys.save()

    External_services.delete()
    context = {
        'External_services': External_services,
    }
    return redirect('External_service_show')

@login_required(login_url="/login/")
def External_services_export(request):
    External_services = External_service.objects.all()
    return render(request,'Asset_Management/External service/export.html',{'External_services':External_services,'segment': 'External Service'} )

@login_required(login_url="/login/")
@user_passes_test(lambda u:u.is_staff, login_url="page-404.html")
def External_services_History(request):
    Historys = History.objects.filter(Database='External_service')
    return render(request,'Asset_Management/External service/History.html',{'Historys':Historys})