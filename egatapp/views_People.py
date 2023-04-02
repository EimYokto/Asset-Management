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

#People

@permission_required("egatapp.view_people", login_url="/login")
def People_show(request):
    Peoples = People.objects.all()
    #Peoples = People.objects.all()#[:5]
    #Peoples = People.objects.filter(position='นักศึกษา')
    return render(request,'Asset_Management/People/DataTable.html',{'Peoples':Peoples} )

@permission_required("egatapp.add_people", login_url="/login")
def People_insert(request):
    if request.method == "POST":
        Employee_Name = request.POST['Employee_Name']
        Employee_ID = request.POST['Employee_ID']
        Section = request.POST['Section']
        Position = request.POST['Position']
        Responsibilities = request.POST['Responsibilities']
        Confidential = request.POST['Confidential']
        Integrity = request.POST['Integrity']
        Availability = request.POST['Availability']
        Contact_Number = request.POST['Contact_Number']
        Email = request.POST['Email']

        USER = request.user
        Database = "People"
        Record = request.POST['Employee_ID']
        ACTION = "Add"

        data = People(Employee_Name=Employee_Name, Employee_ID=Employee_ID, Section=Section, 
        Position=Position, Responsibilities= Responsibilities,Confidential=Confidential,
        Integrity=Integrity,Availability=Availability,Contact_Number=Contact_Number,Email=Email)

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data.save()
        return redirect('People_show')
    else:
        return render(request, 'Asset_Management/People/DataTable.html')

@permission_required("egatapp.change_people", login_url="/login")
def People_edit(request,Employee_ID):
    if request.method == "POST":
        Employee_Name = request.POST.get('Employee_Name')
        Employee_ID = request.POST.get('Employee_ID')
        Section = request.POST.get('Section')
        Position = request.POST.get('Position')
        Responsibilities = request.POST.get('Responsibilities')
        Confidential = request.POST.get('Confidential')
        Integrity = request.POST.get('Integrity')
        Availability = request.POST.get('Availability')
        Contact_Number = request.POST.get('Contact_Number')
        Email = request.POST.get('Email')

        USER = request.user
        Database = "People"
        Record =  request.POST.get('Employee_ID')
        ACTION = "Edit"

        Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
        Historys.save()

        data = People(Employee_Name=Employee_Name, Employee_ID=Employee_ID, Section=Section, 
        Position=Position, Responsibilities= Responsibilities,Confidential=Confidential,
        Integrity=Integrity,Availability=Availability,Contact_Number=Contact_Number,Email=Email)
        data.save()
        return redirect('People_show')
    return redirect(request,'Asset_Management/People/DataTable.html')

@permission_required("egatapp.delete_people", login_url="/login")
def People_delete(request, Employee_ID):
    Peoples = People.objects.filter(Employee_ID = Employee_ID)
    
    USER = request.user
    Database = "People"
    Record = Employee_ID
    ACTION = "Delete"

    Historys = History(USER=USER,Database=Database,Record=Record,ACTION=ACTION)
    Historys.save()
    
    Peoples.delete()
    context = {
        'Peoples': Peoples,
    }
    return redirect('People_show')

@login_required(login_url="/login/")
def People_export(request):
    Peoples = People.objects.all()
    return render(request,'Asset_Management/People/export.html',{'Peoples':Peoples,'segment': 'People'} )

@login_required(login_url="/login/")
@user_passes_test(lambda u:u.is_staff, login_url="page-404.html")
def People_History(request):
    Historys = History.objects.filter(Database='People')
    return render(request,'Asset_Management/People/History.html',{'Historys':Historys})    

#@login_required(login_url="/login/")
# def People_import(request): 
#    if request.method == 'POST':
#        try:
#            file_format = request.POST['file-format']
#            people_resource = PeopleResource()
#            dataset = Dataset()
#            new_people = request.FILES['importData']
#    
#            if file_format == 'CSV':
#                imported_data = dataset.load(new_people.read().decode('utf-8'),format='csv')
#                result = people_resource.import_data(dataset, dry_run=True)                                                                 
#            elif file_format == 'JSON':
#                imported_data = dataset.load(new_people.read().decode('utf-8'),format='json')
#                # Testing data import
#                result = people_resource.import_data(dataset, dry_run=True)
#            else:
#                return render(request, 'Asset_Management/People/import.html',{'error_message': 'Please select format of file.'})  
#            if not result.has_errors():
                # Import now
#                people_resource.import_data(dataset, dry_run=False)
#                return render(request, 'Asset_Management/People/import.html',{'error_message': 'succeed import Data'})
#        except Exception as e:
#            print(e)
#            return render(request, 'Asset_Management/People/import.html',{'error_message': 'File Import Type of File as .CSV .JSON or Please Select File of Attachment.'})    
#    return render(request, 'Asset_Management/People/import.html') 