from import_export import resources
from .models import *

class HardwareResource(resources.ModelResource):
    class Meta:
        model = Hardware
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ("Asset_Code","Asset_Number","Asset_Type","Service"
    ,"Asset_Name","System_Type","Confidential","Integrity","Availability"
    ,"Owner","User","Location","MA_Start","MA_End","Brand_Model","Serial_Number"
    ,"Remark","Description","Asset_Status","Hardware_Type","Software_Version"
    ,"Software_License","Latest_Change","Current_Software_Version","Related_CI"
    ,"Processor_Type","Processor_Speed","Memory_Size","Disk_Size","IP_Address"
    ,"MAC_Address")
class SoftwareResource(resources.ModelResource):
    class Meta:
        model = Software
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ("Asset_Code","Asset_Name"
    ,"Software_Vendor","License_Unit","Asset_Type","System_Type"
    ,"Confidential","Integrity","Availability","Owner","Software_Repository"
    ,"Registered_Date","Asset_Number","Software_Status","Software_Version"
    ,"License_Info","Latest_Change","Latest_Software_Version","Related_CI"
    ,"Vendor_Contact")
class PeopleResource(resources.ModelResource):
    class Meta:
        model = People
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ("Employee_ID","Employee_Name"
    ,"Section","Position","Responsibilities","Confidential"
    ,"Integrity","Availability","Contact_Number","Email")
class InformationResource(resources.ModelResource):
    class Meta:
        model = Information
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ("Asset_Code","Asset_Type"
    ,"System_Name","Asset_Name","Confidential","Integrity"
    ,"Availability","Owner","Info_Repository","Asset_Number"
    ,"Storage_Media","Storage_Period","Responsible_Person")
class In_house_serviceResource(resources.ModelResource):
    class Meta:
        model = In_house_service
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ("Asset_Code","Service_Detail"
    ,"Asset_Type","Confidential","Integrity","Availability"
    ,"Responsible_Person")

class External_serviceResource(resources.ModelResource):
    class Meta:
        model = External_service
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ("Asset_Code","Service_Detail","Vendor_Name"
    ,"Address","Product","Confidential","Integrity","Availability"
    ,"Service_Owner","Contract_Number","Contract_Start_Date","Contract_End_Date"
    ,"Repository","Storage_Media","Phone")
