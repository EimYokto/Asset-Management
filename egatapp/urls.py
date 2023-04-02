from django.urls import path,re_path
from egatapp import views , views_authentication
from egatapp import views_Hardware ,views_Software ,views_People  ,views_Information ,views_In_house_Service ,views_External_Service
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views_authentication.login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_change", views_authentication.password_change, name="password_change"),
    #path("password_change/done", views_authentication.password_change, name="password_change"),
    path("password_reset", views_authentication.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', views_authentication.passwordResetConfirm, name='password_reset_confirm'),

    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),

    # Request For Change Generation
    path('email/', views.EmailAttachementView.as_view(), name='email'),
    path('form/', views.form, name='form'),

    # Hardware Database Add,Edit,Delete,export,import
    path('Hardware_DataTable/', views_Hardware.Hardware_show , name='Hardware_show'),
    path('Hardware_DataTable_insert/', views_Hardware.Hardware_insert , name='Hardware_DataTable_insert'),
    path('Hardware_DataTable_edit/<str:Asset_Code>', views_Hardware.Hardware_edit, name='Hardware_DataTable_edit'),
    path('Hardware_DataTable_delete/<str:Asset_Code>', views_Hardware.Hardware_delete, name='Hardware_DataTable_delete'),
    path('Hardware_export/', views_Hardware.Hardware_export , name='Hardware_export'),
    path('Hardware_History/', views_Hardware.Hardware_History , name='Hardware_History'),
    #path('Hardware_import/', views_Hardware.Hardware_import , name='Hardware_import'),

    # Software Database Add,Edit,Delete,export,import
    path('Software_DataTable/', views_Software.Software_show , name='Software_show'),
    path('Software_DataTable_insert/', views_Software.Software_insert , name='Software_DataTable_insert'),
    path('Software_DataTable_edit/<str:Asset_Code>', views_Software.Software_edit, name='Software_DataTable_edit'),
    path('Software_DataTable_delete/<str:Asset_Code>', views_Software.Software_delete, name='Software_DataTable_delete'),
    path('Software_export/', views_Software.Software_export , name='Software_export'),
    path('Software_History/', views_Software.Software_History , name='Software_History'),
    #path('Software_import/', views_Software.Software_import , name='Software_import'),

    # People Database Add,Edit,Delete,export,import
    path('People_DataTable/', views_People.People_show , name='People_show'),
    path('People_DataTable_insert/', views_People.People_insert , name='People_DataTable_insert'),
    path('People_DataTable_edit/<str:Employee_ID>', views_People.People_edit, name='People_DataTable_edit'),
    path('People_DataTable_delete/<str:Employee_ID>', views_People.People_delete, name='People_DataTable_delete'),
    path('People_export/', views_People.People_export , name='People_export'),
    path('People_History/', views_People.People_History , name='People_History'),

    #path('People_import/', views_People.People_import , name='People_import'),

    # Software Database Add,Edit,Delete,export,import
    path('Information_DataTable/', views_Information.Information_show , name='Information_show'),
    path('Information_DataTable_insert/', views_Information.Information_insert , name='Information_DataTable_insert'),
    path('Information_DataTable_edit/<str:Asset_Code>', views_Information.Information_edit, name='Information_DataTable_edit'),
    path('Information_DataTable_delete/<str:Asset_Code>', views_Information.Information_delete, name='Information_DataTable_delete'),
    path('Information_export/', views_Information.Information_export , name='Information_export'),
    path('Information_History/', views_Information.Information_History , name='Information_History'),
    #path('Information_import/', views_Information.Information_import , name='Information_import'),

    # #In-house Service Database Add,Edit,Delete,export,import
    path('In_house_Service_DataTable/', views_In_house_Service.In_house_Service_show , name='In_house_Service_show'),
    path('In_house_Service_DataTable_insert/', views_In_house_Service.In_house_Service_insert , name='In_house_Service_DataTable_insert'),
    path('In_house_Service_DataTable_edit/<str:Asset_Code>', views_In_house_Service.In_house_Service_edit, name='In_house_Service_DataTable_edit'),
    path('In_house_Service_DataTable_delete/<str:Asset_Code>', views_In_house_Service.In_house_Service_delete, name='In_house_Service_DataTable_delete'),
    path('In_house_Service_export/', views_In_house_Service.In_house_Service_export , name='In_house_Service_export'),
    path('In_house_Service_History/', views_In_house_Service.In_house_Service_History , name='In_house_Service_History'),
    #path('In_house_Service_import/', views_In_house_Service.In_house_Service_import , name='In_house_Service_import'),

    # #In-house Service Database Add,Edit,Delete,export,import
    path('External_service_DataTable/', views_External_Service.External_service_show , name='External_service_show'),
    path('External_service_DataTable_insert/', views_External_Service.External_service_insert , name='External_service_DataTable_insert'),
    path('External_service_DataTable_edit/<str:Asset_Code>', views_External_Service.External_service_edit, name='External_service_DataTable_edit'),
    path('External_service_DataTable_delete/<str:Asset_Code>', views_External_Service.External_service_delete, name='External_service_DataTable_delete'),
    path('External_service_export/', views_External_Service.External_services_export , name='External_service_export'),
    path('External_service_History/', views_External_Service.External_services_History , name='External_service_History'),
    #path('External_service_import/', views_External_Service.External_services_import , name='External_services_import'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    
]