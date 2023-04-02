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

#In-house Service

@permission_required("egatapp.view_in_house_service", login_url="/login")
def In_house_Service_show(request):
    In_house_services = In_house_service.objects.all()
    return render(request,'Asset_Management/In-house Service/DataTable.html',{'In_house_services':In_house_services} )

@permission_required("egatapp.add_in_house_service", login_url="/login")
def In_house_Service_insert(request):
    if request.method == "POST":
        Asset_Code = None
        Service_Detail = request.POST['Service_Detail']
        Asset_Type = request.POST['Asset_Type']
        Confidential = request.POST['Confidential']
        Integrity = request.POST['Integrity']
        Availability = request.POST['Availability']
        Responsible_Person = request.POST['Responsible_Person']

        last_In_house_service = In_house_service.objects.count()
        last_pk = 0
        if last_In_house_service:
            last_pk = last_In_house_service

        Asset_Code_Historys = "D403021-" + "SER-" + str(last_pk+1).zfill(5)

        USER = request.user
        Database = "In-house_Service"
        Record = Asset_Code_Historys
        ACTION = "Add"

        data = In_house_service(Asset_Code=Asset_Code,Service_Detail=Service_Detail, Asset_Type=Asset_Type, 
        Confidential=Confidential,Integrity=Integrity,Availability=Availability,
        Responsible_Person=Responsible_Person)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('In_house_Service_show')
    else:
        return render(request, 'Asset_Management/In-house Service/DataTable.html')

@permission_required("egatapp.change_in_house_service", login_url="/login")
def In_house_Service_edit(request,Asset_Code):
    if request.method == "POST":
        Asset_Code = request.POST.get('Asset_Code')
        Service_Detail = request.POST.get('Service_Detail')
        Asset_Type = request.POST.get('Asset_Type')
        Confidential = request.POST.get('Confidential')
        Integrity = request.POST.get('Integrity')
        Availability = request.POST.get('Availability')
        Responsible_Person = request.POST.get('Responsible_Person')

        USER = request.user
        Database = "In-house_Service"
        Record =  request.POST.get('Asset_Code')
        ACTION = "Edit"

        data = In_house_service(Asset_Code=Asset_Code, Service_Detail=Service_Detail, Asset_Type=Asset_Type, 
        Confidential=Confidential,Integrity=Integrity,Availability=Availability,
        Responsible_Person=Responsible_Person)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('In_house_Service_show')
    return redirect(request,'Asset_Management/In-house Service/DataTable.html')

@permission_required("egatapp.delete_in_house_service", login_url="/login")
def In_house_Service_delete(request,Asset_Code):
    In_house_services = In_house_service.objects.filter(Asset_Code = Asset_Code)

    USER = request.user
    Database = "In-house_Service"
    Record = Asset_Code
    ACTION = "Delete"

    Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
    Historys.save()

    In_house_services.delete()
    context = {
        'In_house_services': In_house_services,
    }
    return redirect('In_house_Service_show')

@login_required(login_url="/login/")
def In_house_Service_export(request):
    In_house_services = In_house_service.objects.all()
    return render(request,'Asset_Management/In-house Service/export.html',{'In_house_services':In_house_services,'segment': 'In-House Service'} )

@login_required(login_url="/login/")
@user_passes_test(lambda u:u.is_staff, login_url="page-404.html")
def In_house_Service_History(request):
    Historys = History.objects.filter(Database='In-house_Service')
    return render(request,'Asset_Management/In-house Service/History.html',{'Historys':Historys})