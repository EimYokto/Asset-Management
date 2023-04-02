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

#Hardware

@permission_required("egatapp.view_hardware", login_url="/login")
def Hardware_show(request):
    Hardwares = Hardware.objects.all()
    return render(request,'Asset_Management/Hardware/DataTable.html',{'Hardwares':Hardwares} )

@permission_required("egatapp.add_hardware", login_url="/login")
def Hardware_insert(request):
    if request.method == "POST":
        Asset_Code = None
        Asset_Number = request.POST['Asset_Number']
        Asset_Type = request.POST['Asset_Type']
        Service = request.POST['Service']
        Asset_Name = request.POST['Asset_Name']
        System_Type = request.POST['System_Type']
        Confidential = request.POST['Confidential']
        Integrity = request.POST['Integrity']
        Availability = request.POST['Availability']
        Owner = request.POST['Owner']
        User = request.POST['User']
        Location = request.POST['Location']
        MA_Start =request.POST['MA_Start']
        MA_End = request.POST['MA_End']
        Brand_Model = request.POST['Brand_Model']
        Serial_Number = request.POST['Serial_Number']
        Remark = request.POST['Remark']
        Description = request.POST['Description']
        Asset_Status = request.POST['Asset_Status']
        Hardware_Type = request.POST['Hardware_Type']
        Software_Version = request.POST['Software_Version']
        Software_License = request.POST['Software_License']
        Latest_Change = request.POST['Latest_Change']
        Current_Software_Version = request.POST['Current_Software_Version']
        Related_CI = request.POST['Related_CI']
        Processor_Type = request.POST['Processor_Type']
        Processor_Speed = request.POST['Processor_Speed']
        Memory_Size = request.POST['Memory_Size']
        Disk_Size = request.POST['Disk_Size']
        IP_Address = request.POST['IP_Address']
        MAC_Address = request.POST['MAC_Address']

        last_Hardware = Hardware.objects.count()
        last_pk = 0
        if last_Hardware:
            last_pk = last_Hardware
            
        Asset_Code_Historys = "D403021-" + "HAR-" + str(last_pk+1).zfill(5)

        USER = request.user
        Database = "Hardware"
        Record = Asset_Code_Historys
        ACTION = "Add"

        data = Hardware(Asset_Code=Asset_Code, Asset_Number=Asset_Number, Asset_Type=Asset_Type, 
        Service=Service, Asset_Name= Asset_Name,System_Type=System_Type,Confidential=Confidential,
        Integrity=Integrity,Availability=Availability,Owner=Owner,User=User,Location=Location,
        MA_Start=MA_Start,MA_End=MA_End,Brand_Model=Brand_Model,Serial_Number=Serial_Number,
        Remark=Remark,Description=Description,Asset_Status=Asset_Status,Hardware_Type=Hardware_Type,
        Software_Version=Software_Version,Software_License=Software_License,Latest_Change=Latest_Change,
        Current_Software_Version=Current_Software_Version,Related_CI=Related_CI,
        Processor_Type=Processor_Type,Processor_Speed=Processor_Speed,Memory_Size=Memory_Size,
        Disk_Size=Disk_Size,IP_Address=IP_Address,MAC_Address=MAC_Address)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('Hardware_show')
    else:
        return render(request, 'Asset_Management/Hardware/DataTable.html')

@permission_required("egatapp.change_hardware", login_url="/login")
def Hardware_edit(request,Asset_Code):
    if request.method == "POST":
        Asset_Code = request.POST.get('Asset_Code')
        Asset_Number = request.POST.get('Asset_Number')
        Asset_Type = request.POST.get('Asset_Type')
        Service = request.POST.get('Service')
        Asset_Name = request.POST.get('Asset_Name')
        System_Type = request.POST.get('System_Type')
        Confidential = request.POST.get('Confidential')
        Integrity = request.POST.get('Integrity')
        Availability = request.POST.get('Availability')
        Owner = request.POST.get('Owner')
        User = request.POST.get('User')
        Location = request.POST.get('Location')
        MA_Start =request.POST.get('MA_Start')
        MA_End = request.POST.get('MA_End')
        Brand_Model = request.POST.get('Brand_Model')
        Serial_Number = request.POST.get('Serial_Number')
        Remark = request.POST.get('Remark')
        Description = request.POST.get('Description')
        Asset_Status = request.POST.get('Asset_Status')
        Hardware_Type = request.POST.get('Hardware_Type')
        Software_Version = request.POST.get('Software_Version')
        Software_License = request.POST.get('Software_License')
        Latest_Change = request.POST.get('Latest_Change')
        Current_Software_Version = request.POST.get('Current_Software_Version')
        Related_CI = request.POST.get('Related_CI')
        Processor_Type = request.POST.get('Processor_Type')
        Processor_Speed = request.POST.get('Processor_Speed')
        Memory_Size = request.POST.get('Memory_Size')
        Disk_Size = request.POST.get('Disk_Size')
        IP_Address = request.POST.get('IP_Address')
        MAC_Address = request.POST.get('MAC_Address')

        USER = request.user
        Database = "Hardware"
        Record =  request.POST.get('Asset_Code')
        ACTION = "Edit"

        data = Hardware(Asset_Code=Asset_Code, Asset_Number=Asset_Number, Asset_Type=Asset_Type, 
        Service=Service, Asset_Name= Asset_Name,System_Type=System_Type,Confidential=Confidential,
        Integrity=Integrity,Availability=Availability,Owner=Owner,User=User,Location=Location,
        MA_Start=MA_Start,MA_End=MA_End,Brand_Model=Brand_Model,Serial_Number=Serial_Number,
        Remark=Remark,Description=Description,Asset_Status=Asset_Status,Hardware_Type=Hardware_Type,
        Software_Version=Software_Version,Software_License=Software_License,Latest_Change=Latest_Change,
        Current_Software_Version=Current_Software_Version,Related_CI=Related_CI,
        Processor_Type=Processor_Type,Processor_Speed=Processor_Speed,Memory_Size=Memory_Size,
        Disk_Size=Disk_Size,IP_Address=IP_Address,MAC_Address=MAC_Address)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('Hardware_show')
    return redirect(request,'Asset_Management/Hardware/DataTable.html')

@permission_required("egatapp.delete_hardware", login_url="/login")
def Hardware_delete(request,Asset_Code):
    Hardwares = Hardware.objects.filter(Asset_Code = Asset_Code)

    USER = request.user
    Database = "Hardware"
    Record = Asset_Code
    ACTION = "Delete"

    Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
    Historys.save()

    Hardwares.delete()
    context = {
        'Hardwares': Hardwares,
    }
    return redirect('Hardware_show')

@login_required(login_url="/login/")
def Hardware_export(request):
    Hardwares = Hardware.objects.all()
    return render(request,'Asset_Management/Hardware/export.html',{'Hardwares':Hardwares,'segment': 'Hardware'} )

@login_required(login_url="/login/")
@user_passes_test(lambda u:u.is_staff, login_url="page-404.html")
def Hardware_History(request):
    Historys = History.objects.filter(Database='Hardware')
    return render(request,'Asset_Management/Hardware/History.html',{'Historys':Historys})