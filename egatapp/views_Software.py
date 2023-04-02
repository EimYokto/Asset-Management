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

#Software

@permission_required("egatapp.view_software", login_url="/login")
def Software_show(request):
    Softwares = Software.objects.all()
    return render(request,'Asset_Management/Software/DataTable.html',{'Softwares':Softwares} )

@permission_required("egatapp.add_software", login_url="/login")
def Software_insert(request):
    if request.method == "POST":
        Asset_Code = None
        Asset_Name = request.POST['Asset_Name']
        Software_Vendor = request.POST['Software_Vendor']
        License_Unit = request.POST['License_Unit']
        Asset_Type = request.POST['Asset_Type']
        System_Type = request.POST['System_Type']
        Confidential = request.POST['Confidential']
        Integrity = request.POST['Integrity']
        Availability = request.POST['Availability']
        Owner = request.POST['Owner']
        Software_Repository = request.POST['Software_Repository']
        Registered_Date = request.POST['Registered_Date']
        Asset_Number= request.POST['Asset_Number']
        Software_Status = request.POST['Software_Status']
        Software_Version = request.POST['Software_Version']
        License_Info = request.POST['License_Info']
        Latest_Change = request.POST['Latest_Change']
        Latest_Software_Version = request.POST['Latest_Software_Version']
        Related_CI = request.POST['Related_CI']
        Vendor_Contact = request.POST['Vendor_Contact']

        last_Software = Software.objects.count()
        last_pk = 0
        if last_Software:
            last_pk = last_Software

        Asset_Code_Historys = "D403021-" + "SOF-" + str(last_pk+1).zfill(5)

        USER = request.user
        Database = "Software"
        Record = Asset_Code_Historys
        ACTION = "Add"

        data = Software(Asset_Code=Asset_Code, Asset_Name=Asset_Name, Software_Vendor=Software_Vendor, 
        License_Unit=License_Unit, Asset_Type= Asset_Type,System_Type=System_Type,Confidential=Confidential,
        Integrity=Integrity,Availability=Availability,Owner=Owner,Software_Repository=Software_Repository,
        Registered_Date=Registered_Date,Asset_Number=Asset_Number,Software_Status=Software_Status,
        Software_Version=Software_Version,License_Info=License_Info,Latest_Change=Latest_Change,
        Latest_Software_Version=Latest_Software_Version,Related_CI=Related_CI,Vendor_Contact=Vendor_Contact,)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('Software_show')
    else:
        return render(request, 'Asset_Management/Software/DataTable.html')

@permission_required("egatapp.change_software", login_url="/login")
def Software_edit(request,Asset_Code):
    if request.method == "POST":
        Asset_Code = request.POST.get('Asset_Code')
        Asset_Name = request.POST.get('Asset_Name')
        Software_Vendor = request.POST.get('Software_Vendor')
        License_Unit = request.POST.get('License_Unit')
        Asset_Type = request.POST.get('Asset_Type')
        System_Type = request.POST.get('System_Type')
        Confidential = request.POST.get('Confidential')
        Integrity = request.POST.get('Integrity')
        Availability = request.POST.get('Availability')
        Owner = request.POST.get('Owner')
        Software_Repository = request.POST.get('Software_Repository')
        Registered_Date = request.POST.get('Registered_Date')
        Asset_Number = request.POST.get('Asset_Number')
        Software_Status = request.POST.get('Software_Status')
        Software_Version = request.POST.get('Software_Version')
        License_Info = request.POST.get('License_Info')
        Latest_Change = request.POST.get('Latest_Change')
        Latest_Software_Version = request.POST.get('Latest_Software_Version')
        Related_CI = request.POST.get('Related_CI')
        Vendor_Contact = request.POST.get('Vendor_Contact')

        USER = request.user
        Database = "Software"
        Record = request.POST['Asset_Code']
        ACTION = "Edit"

        data = Software(Asset_Code=Asset_Code, Asset_Name=Asset_Name, Software_Vendor=Software_Vendor, 
        License_Unit=License_Unit, Asset_Type= Asset_Type,System_Type=System_Type,Confidential=Confidential,
        Integrity=Integrity,Availability=Availability,Owner=Owner,Software_Repository=Software_Repository,
        Registered_Date=Registered_Date,Asset_Number=Asset_Number,Software_Status=Software_Status,
        Software_Version=Software_Version,License_Info=License_Info,Latest_Change=Latest_Change,
        Latest_Software_Version=Latest_Software_Version,Related_CI=Related_CI,Vendor_Contact=Vendor_Contact,)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('Software_show')
    return redirect(request,'Asset_Management/Software/DataTable.html')

@permission_required("egatapp.delete_software", login_url="/login")
def Software_delete(request,Asset_Code):
    Softwares = Software.objects.filter(Asset_Code = Asset_Code)

    USER = request.user
    Database = "Software"
    Record = Asset_Code
    ACTION = "Delete"

    Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
    Historys.save()

    Softwares.delete()
    context = {
        'Softwares': Softwares,
    }
    return redirect('Software_show')

@login_required(login_url="/login/")
def Software_export(request):
    Softwares = Software.objects.all()
    return render(request,'Asset_Management/Software/export.html',{'Softwares':Softwares,'segment': 'Software'})

@login_required(login_url="/login/")
@user_passes_test(lambda u:u.is_staff, login_url="page-404.html")
def Software_History(request):
    Historys = History.objects.filter(Database='Software')
    return render(request,'Asset_Management/Software/History.html',{'Historys':Historys})