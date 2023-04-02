from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin ,ExportActionMixin
from .resources import *
# Register your models here.

admin.site.disable_action('delete_selected')
@admin.register(Hardware)
class HardwareAdmin(ImportExportModelAdmin,ExportActionMixin, admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ["Asset_Code"]
    pass
    resource_class = HardwareResource
    list_display = ("Asset_Code","Asset_Number","Asset_Type","Service"
    ,"Asset_Name","System_Type","Confidential","Integrity","Availability"
    ,"Owner","User","Location","MA_Start","MA_End","Brand_Model","Serial_Number"
    ,"Remark","Description","Asset_Status","Hardware_Type","Software_Version"
    ,"Software_License","Latest_Change","Current_Software_Version","Related_CI"
    ,"Processor_Type","Processor_Speed","Memory_Size","Disk_Size","IP_Address"
    ,"MAC_Address")
    list_per_page = 10
@admin.register(Software)
class SoftwareAdmin(ImportExportModelAdmin,ExportActionMixin, admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ["Asset_Code"]
    pass
    resource_class = SoftwareResource
    list_display = ("Asset_Code","Asset_Name"
    ,"Software_Vendor","License_Unit","Asset_Type","System_Type"
    ,"Confidential","Integrity","Availability","Owner","Software_Repository"
    ,"Registered_Date","Asset_Number","Software_Status","Software_Version"
    ,"License_Info","Latest_Change","Latest_Software_Version","Related_CI"
    ,"Vendor_Contact")
    list_per_page = 10
@admin.register(People)
class PeopleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ["Employee_ID"]
    pass
    resource_class = PeopleResource
    list_display = ("Employee_ID","Employee_Name"
    ,"Section","Position","Responsibilities","Confidential"
    ,"Integrity","Availability","Contact_Number","Email")
    list_per_page = 10

@admin.register(Information)
class InformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ["Asset_Code"]
    pass    
    resource_class = InformationResource
    list_display = ("Asset_Code","Asset_Type"
    ,"System_Name","Asset_Name","Confidential","Integrity"
    ,"Availability","Owner","Info_Repository","Asset_Number"
    ,"Storage_Media","Storage_Period","Responsible_Person")
    list_per_page = 10
@admin.register(In_house_service)
class In_house_serviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ["Asset_Code"]
    pass    
    resource_class = In_house_serviceResource
    list_display = ("Asset_Code","Service_Detail"
    ,"Asset_Type","Confidential","Integrity","Availability"
    ,"Responsible_Person")
    list_per_page = 10
@admin.register(External_service)
class External_serviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ["Asset_Code"]
    pass    
    resource_class = External_serviceResource
    list_display =("Asset_Code","Service_Detail","Vendor_Name"
    ,"Address","Product","Confidential","Integrity","Availability"
    ,"Service_Owner","Contract_Number","Contract_Start_Date","Contract_End_Date"
    ,"Repository","Storage_Media","Phone")
    list_per_page = 10
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass
    def has_add_permission(self, request, obj=None):
        return False
    list_display = ( "USER","Database","Record","ACTION","DATE_TIME")
    list_per_page = 10



