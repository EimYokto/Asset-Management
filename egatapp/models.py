from django.db import models
from django.contrib.auth.models import User

CIA = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
)
# Create your models here.
class Hardware(models.Model):
    Hardware_Status= (
        ('Decommissioned', 'Decommissioned'),
        ('Operating','Operating'),
        ('Not Ready','Not Ready'),
    )
    Asset_Code = models.CharField(primary_key=True,max_length=255)
    Asset_Number = models.CharField(max_length=100)
    Asset_Type = models.CharField(max_length=100)
    Service = models.CharField(max_length=100)
    Asset_Name = models.CharField(max_length=100)
    System_Type = models.CharField(max_length=100)
    Confidential = models.IntegerField(choices=CIA)
    Integrity = models.IntegerField(choices=CIA)
    Availability = models.IntegerField(choices=CIA)
    Owner = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    MA_Start = models.DateField()
    MA_End = models.DateField()
    Brand_Model = models.CharField(max_length=100)
    Serial_Number = models.CharField(max_length=100)
    Remark = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Asset_Status = models.CharField(choices= Hardware_Status,max_length=100)
    Hardware_Type = models.CharField(max_length=100)
    Software_Version = models.CharField(max_length=100)
    Software_License = models.CharField(max_length=100)
    Latest_Change = models.CharField(max_length=100)
    Current_Software_Version = models.CharField(max_length=100)
    Related_CI = models.CharField(max_length=100)
    Processor_Type = models.CharField(max_length=100)
    Processor_Speed = models.CharField(max_length=100)
    Memory_Size = models.CharField(max_length=100)
    Disk_Size = models.CharField(max_length=100)
    IP_Address = models.GenericIPAddressField(max_length=100)
    MAC_Address = models.CharField(max_length=100)

    def save(self):
        if not self.Asset_Code and self.pk is None:
            print('456asd')
            last_Hardware = Hardware.objects.count()
            last_pk = 0
            if last_Hardware:
                last_pk = last_Hardware

            self.Asset_Code = "D403021-" + "HAR-" + str(last_pk+1).zfill(5)
        super(Hardware, self).save()
    class Meta:
        db_table="Hardware"
    #    permissions = (('import_Hardware', 'Can import Hardware'), ('export_Hardware', 'Can export Hardware'))

class Software(models.Model):
    Software_Status= (
            ('Available', 'Available'),
            ('UnAvailable', 'UnAvailable'),
    )
    Asset_Code = models.CharField(primary_key=True,max_length=100)
    Asset_Name = models.CharField(max_length=100)
    Software_Vendor = models.CharField(max_length=100)	
    License_Unit = models.IntegerField()	
    Asset_Type = models.CharField(max_length=100)	
    System_Type = models.CharField(max_length=100)	
    Confidential = models.IntegerField(choices=CIA)
    Integrity = models.IntegerField(choices=CIA)
    Availability = models.IntegerField(choices=CIA)
    Owner = models.CharField(max_length=100)
    Software_Repository = models.CharField(max_length=100)	
    Registered_Date = models.DateField()	
    Asset_Number = models.CharField(max_length=100)
    Software_Status  = models.CharField(
        choices=Software_Status,max_length=100
    )
    Software_Version = models.CharField(max_length=100)	
    License_Info = models.CharField(max_length=100)	
    Latest_Change = models.CharField(max_length=100)	
    Latest_Software_Version = models.CharField(max_length=100)	
    Related_CI = models.CharField(max_length=100)
    Vendor_Contact = models.CharField(max_length=100)

    def save(self):
        if not self.Asset_Code and self.pk is None:
            print('456asd')
            last_Software = Software.objects.count()
            last_pk = 0
            if last_Software:
                last_pk = last_Software

            self.Asset_Code = "D403021-" + "SOF-" + str(last_pk+1).zfill(5)
        super(Software, self).save()
    class Meta:
        db_table="Software"
    #    permissions = (('import_Software', 'Can import Software'), ('export_Software', 'Can export Software'))

class People(models.Model):
    Responsibilities= (
            ('หัวหน้าแผนก', 'หัวหน้าแผนก'),
            ('เจ้าหน้าที่รับผิดชอบระบบงาน', 'เจ้าหน้าที่รับผิดชอบระบบงาน'),
    )
    Employee_ID = models.CharField(primary_key=True,max_length=100)
    Employee_Name = models.CharField(max_length=100)
    Section = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Responsibilities = models.CharField(
        choices=Responsibilities,max_length=100
    )
    Confidential = models.IntegerField(choices=CIA)
    Integrity = models.IntegerField(choices=CIA)
    Availability = models.IntegerField(choices=CIA)
    Contact_Number = models.CharField(max_length=100)
    Email = models.EmailField()
    class Meta:
        db_table="People"
    #    permissions = (('import_People', 'Can import People'), ('export_People', 'Can export People'))

class Information(models.Model):
    Asset_Code = models.CharField(primary_key=True,max_length=100)	
    Asset_Type = models.CharField(max_length=100)	
    System_Name = models.CharField(max_length=100)	
    Asset_Name = models.CharField(max_length=100)	
    Confidential = models.IntegerField(choices=CIA)
    Integrity = models.IntegerField(choices=CIA)
    Availability = models.IntegerField(choices=CIA)	
    Owner = models.CharField(max_length=100)	
    Info_Repository = models.CharField(max_length=100)	
    Asset_Number = models.CharField(max_length=100)	
    Storage_Media = models.CharField(max_length=100)	
    Storage_Period = models.CharField(max_length=100)	
    Responsible_Person = models.CharField(max_length=100)

    def save(self):
        if not self.Asset_Code and self.pk is None:
            print('456asd')
            last_Information = Information.objects.count()
            last_pk = 0
            if last_Information:
                last_pk = last_Information

            self.Asset_Code = "D403021-" + "INF-" + str(last_pk+1).zfill(5)
        super(Information, self).save()
    class Meta:
        db_table="Information"
    #    permissions = (('import_Information', 'Can import Information'), ('export_Information', 'Can export Information'))

class In_house_service(models.Model): 
    Asset_Code = models.CharField(primary_key=True,max_length=100)	
    Service_Detail = models.CharField(max_length=100)	
    Asset_Type = models.CharField(max_length=100)	
    Confidential = models.IntegerField(choices=CIA)
    Integrity = models.IntegerField(choices=CIA)
    Availability = models.IntegerField(choices=CIA)	
    Responsible_Person = models.CharField(max_length=100)
    
    def save(self):
        if not self.Asset_Code and self.pk is None:
            print('456asd')
            last_In_house_service = In_house_service.objects.count()
            last_pk = 0
            if last_In_house_service:
                last_pk = last_In_house_service

            self.Asset_Code = "D403021-" + "SER-" + str(last_pk+1).zfill(5)
        super(In_house_service, self).save()
    class Meta:
        db_table="In_house_service"
    #    permissions = (('import_In_house_service', 'Can import In_house_service'), ('export_In_house_service', 'Can export In_house_service'))
class External_service(models.Model): 
    Asset_Code = models.CharField(primary_key=True,max_length=100)	
    Service_Detail = models.CharField(max_length=100)	
    Vendor_Name = models.CharField(max_length=100)	
    Address = models.CharField(max_length=100)	
    Product = models.CharField(max_length=100)	
    Confidential = models.IntegerField(choices=CIA)
    Integrity = models.IntegerField(choices=CIA)
    Availability = models.IntegerField(choices=CIA)	
    Service_Owner = models.CharField(max_length=100)	
    Contract_Number = models.CharField(max_length=100)
    Contract_Start_Date = models.DateField()	
    Contract_End_Date = models.DateField()	
    Repository = models.CharField(max_length=100)	
    Storage_Media = models.CharField(max_length=100)	
    Phone = models.CharField(max_length=100)

    def save(self):
        if not self.Asset_Code and self.pk is None:
            print('456asd')
            last_External_service = External_service.objects.count()
            last_pk = 0
            if last_External_service:
                last_pk = last_External_service

            self.Asset_Code = "D403021-" + "ESER-" + str(last_pk+1).zfill(5)
        super(External_service, self).save()
    class Meta:
        db_table="External_service"
    #    permissions = (('import_External_service', 'Can import External_service'), ('export_External_service', 'Can export External_service'))

class History(models.Model): 
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Database = models.CharField(max_length=100)
    Record = models.CharField(max_length=100)
    ACTION = models.CharField(max_length=100)
    DATE_TIME = models.DateTimeField(auto_now_add=True, blank=True)	
    class Meta:
        db_table="History"