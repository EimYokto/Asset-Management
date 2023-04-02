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

#Information

@permission_required("egatapp.view_information", login_url="/login")
def Information_show(request):
    Informations = Information.objects.all()
    return render(request,'Asset_Management/Information/DataTable.html',{'Informations':Informations} )

@permission_required("egatapp.add_information", login_url="/login")
def Information_insert(request):
    if request.method == "POST":
        Asset_Code = None
        Asset_Type = request.POST['Asset_Type']
        System_Name = request.POST['System_Name']
        Asset_Name = request.POST['Asset_Name']
        Confidential = request.POST['Confidential']
        Integrity = request.POST['Integrity']
        Availability = request.POST['Availability']
        Owner = request.POST['Owner']
        Info_Repository = request.POST['Info_Repository']
        Asset_Number = request.POST['Asset_Number']
        Storage_Media = request.POST['Storage_Media']
        Storage_Period = request.POST['Storage_Period']
        Responsible_Person= request.POST['Responsible_Person']

        last_Information = Information.objects.count()
        last_pk = 0
        if last_Information:
            last_pk = last_Information

        Asset_Code_Historys = "D403021-" + "INF-" + str(last_pk+1).zfill(5)

        USER = request.user
        Database = "Information"
        Record = Asset_Code_Historys
        ACTION = "Add"

        data = Information(Asset_Code=Asset_Code, Asset_Type=Asset_Type, System_Name=System_Name, 
        Asset_Name=Asset_Name, Confidential= Confidential,Integrity=Integrity,Availability=Availability,
        Owner=Owner,Info_Repository=Info_Repository,Asset_Number=Asset_Number,Storage_Media=Storage_Media,
        Storage_Period=Storage_Period,Responsible_Person=Responsible_Person,)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('Information_show')
    else:
        return render(request, 'Asset_Management/Information/DataTable.html')

@permission_required("egatapp.change_information", login_url="/login")
def Information_edit(request,Asset_Code):
    if request.method == "POST":
        Asset_Code = request.POST.get('Asset_Code')
        Asset_Type = request.POST.get('Asset_Type')
        System_Name = request.POST.get('System_Name')
        Asset_Name = request.POST.get('Asset_Name')
        Confidential = request.POST.get('Confidential')
        Integrity = request.POST.get('Integrity')
        Availability = request.POST.get('Availability')
        Owner = request.POST.get('Owner')
        Info_Repository = request.POST.get('Info_Repository')
        Asset_Number = request.POST.get('Asset_Number')
        Storage_Media = request.POST.get('Storage_Media')
        Storage_Period = request.POST.get('Storage_Period')
        Responsible_Person= request.POST.get('Responsible_Person')

        USER = request.user
        Database = "Information"
        Record =  request.POST.get('Asset_Code')
        ACTION = "Edit"

        data = Information(Asset_Code=Asset_Code, Asset_Type=Asset_Type, System_Name=System_Name, 
        Asset_Name=Asset_Name, Confidential= Confidential,Integrity=Integrity,Availability=Availability,
        Owner=Owner,Info_Repository=Info_Repository,Asset_Number=Asset_Number,Storage_Media=Storage_Media,
        Storage_Period=Storage_Period,Responsible_Person=Responsible_Person,)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('Information_show')
    return redirect(request,'Asset_Management/Information/DataTable.html')

@permission_required("egatapp.delete_information", login_url="/login")
def Information_delete(request,Asset_Code):
    Informations = Information.objects.filter(Asset_Code = Asset_Code)

    USER = request.user
    Database = "Information"
    Record = Asset_Code
    ACTION = "Delete"

    Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
    Historys.save()

    Informations.delete()
    context = {
        'Informations': Informations,
    }
    return redirect('Information_show')

@login_required(login_url="/login/")
def Information_export(request):
    Informations = Information.objects.all()
    return render(request,'Asset_Management/Information/export.html',{'Informations':Informations,'segment': 'Information'} )

@login_required(login_url="/login/")
@user_passes_test(lambda u:u.is_staff, login_url="page-404.html")
def Information_History(request):
    Historys = History.objects.filter(Database='Information')
    return render(request,'Asset_Management/Information/History.html',{'Historys':Historys})