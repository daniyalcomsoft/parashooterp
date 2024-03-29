"""parashooterp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, Hod_views, Staff_views, Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login Path 
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('hod/Home', views.HOME, name='hod_home'),
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    path('add/company/', views.Add_Company, name='add_company'),
    path('view/company/', views.View_Company, name='view_company'),
    path('edit/company/<str:id>', views.Edit_Company, name='edit_company'),
    path('update/company/', views.Update_Company, name='update_company'),
    path('delete/company/<str:id>', views.Delete_Company, name="delete_company"),

    path('add/endcompany/', views.Add_EndCompany, name='add_endcompany'),
    path('view/endcompany/', views.View_EndCompany, name='view_endcompany'),
    path('edit/endcompany/<str:id>', views.Edit_EndCompany, name='edit_endcompany'),
    path('update/endcompany/', views.Update_EndCompany, name='update_endcompany'),
    path('delete/endcompany/<str:id>', views.Delete_EndCompany, name='delete_endcompany'),

    

    path('add/engg/', views.Add_Engg, name='add_engg'),
    path('view/engg/', views.View_Engg, name='view_engg'),
    path('edit/engg/<str:id>', views.Edit_Engg, name='edit_engg'),
    path('update/engg/', views.Update_Engg, name='update_engg'),
    path('delete/engg/<str:id>', views.Delete_Engg, name='delete_engg'),

    path('add/contractSLA/', views.Add_ContractSLA, name="add_contractSLA"),
    path('view/contractSLA/', views.View_ContractSLA, name="view_contractSLA"),
    path('edit/contractSLA/<str:id>', views.Edit_ContractSLA, name="edit_contractSLA"),
    path('update/contractSLA/', views.Update_ContractSLA, name="update_contractSLA"),
    path('delete/contractSLA/<str:id>', views.Delete_ContractSLA, name='delete_contractSLA'),


    path('add/contractType/', views.Add_ContractType, name="add_contractType"),
    path('view/contractType', views.View_ContractType, name="view_contractType"),
    path('edit/contractType/<str:id>', views.Edit_ContractType, name="edit_contractType"),
    path('update/contractType', views.Update_ContractType, name="update_contractType"),
    path('delete/contractType/<str:id>', views.Delete_ContractType, name="delete_contractType"),

    path('add/contractSubType/', views.Add_ContractSubType, name="add_contractSubType"),
    path('view/contractSubType/', views.View_ContractSubType, name="view_contractSubType"),
    path('edit/contractSubType/<str:id>', views.Edit_ContractSubType, name="edit_contractSubType"),
    path('update/contractSubType/', views.Update_ContractSubType, name="update_contractSubType"),
    path('delete/contractSubType/<str:id>', views.Delete_ContractSubType, name="delete_contractSubType"),

    path('add/contractStatus/', views.Add_ContractStatus, name="add_contractStatus"),
    path('view/contractStatus/', views.View_ContractStatus, name='view_contractStatus'),
    path('edit/contractStauts/<str:id>', views.Edit_ContractStatus, name="edit_contractStatus"),
    path('update/contractStatus/', views.Update_ContractStatus, name="update_contractStatus"),
    path('delete/contractStauts/<str:id>', views.Delete_ContractStatus, name="delete_contractStatus"),
    
    path('add/contract/', views.Add_Contract, name="add_contract"),
    path('view/contract', views.View_Contract, name="view_contract"),
    path('edit/contract/<str:id>', views.Edit_Contract, name="edit_contract"),
    path('update/contract/', views.Update_Contract, name="update_contract"),
    path('delete/contract/<str:id>', views.Delete_Contract, name="delete_contract"),

    
    path('add/projectType/', views.Add_ProjectType, name='add_projectType'),
    path('view/projectType/', views.View_ProjectType, name="view_projectType"),
    path('edit/projectType/<str:id>', views.Edit_ProjectType, name='edit_projectType'),
    path('update/projectType/', views.Update_ProjectType, name='update_projectType'),
    path('delete/projectType/<str:id>', views.Delete_ProjectType, name='delete_projectType'),

    path('add/projectSubType/', views.Add_ProjectSubType, name='add_projectSubType'),
    path('view/projectSubType/', views.View_ProjectSubType, name='view_projectSubType'),

    path('add/projectStatus/', views.Add_ProjectStatus, name='add_projectStatus'),
    path('view/projectStatus/', views.View_ProjectStatus, name='view_projectStatus'),
    path('edit/projectStatus/<str:id>', views.Edit_ProjectStatus, name='edit_projectStatus'),
    path('update/projectStatus/', views.Update_ProjectStauts, name="update_projectStatus"),
    path('delete/projectStatus/<str:id>', views.Delete_ProjectStatus, name="delete_projectStatus"),

    path('add/project/', views.Add_Project, name='add_project'),
    path('view/project/', views.View_Project, name="view_project"),
    path('edit/project/<str:id>', views.Edit_Project, name="edit_project"),
    path('update/project/', views.Update_Project, name="update_project"),
    path('delete/project/<str:id>', views.Delete_Project, name="delete_project"),

    path('add/ticketStatus/', views.Add_TicketStatus, name='add_ticketStatus'),
    path('view/ticketStatus', views.View_TicketStatus, name='view_ticketStatus'),
    path('edit/ticketStatus/<str:id>', views.Edit_TicketStatus, name='edit_ticketStatus'),
    path('update/ticketStatus/', views.Update_TicketStatus, name='update_ticketStatus'),
    path('delete/ticketStatus/<str:id>', views.Delete_TicketStatus, name='delete_ticketStatus'),

    path('add/ticketStatusHis/', views.Add_TicketStatusHis, name='add_ticketStatusHis'),

    path('add/ticketType/', views.Add_TicketType, name='add_ticketType'),
    path('view/ticketType/', views.View_TicketType, name='view_ticketType'),
    path('edit/ticketType/<str:id>', views.Edit_TicketType, name='edit_ticketType'),
    path('update/ticketType/', views.Update_TicketType, name='update_ticketType'),
    path('delete/ticketType/<str:id>', views.Delete_TicketType, name='delete_ticketType'),

    path('add/billable/', views.Add_Billable, name='add_billable'),
    path('views/billable/', views.View_Billable, name='view_billable'),
    path('edit/billable/<str:id>', views.Edit_Billable, name='edit_billable'),
    path('update/billable/', views.Update_Billable, name='update_billable'),
    path('delete/billable/<str:id>', views.Delete_Billable, name='delete_billable'),

    
    path('add/ticket/', views.Add_Ticket, name='add_ticket'),
    path('view/ticket', views.View_Ticket, name='view_ticket'),
    path('edit/ticket/<str:id>', views.Edit_Ticket, name="edit_ticket"),

    path('add/ticektAdminStatus/', views.Add_TicketAdminStatus, name='add_ticketAdminStatus'),
    path('view/ticketAdminStatus/', views.View_TicketAdminStatus, name='view_ticketAdminStatus'),
    path('edit/ticketAdminStatus/<str:id>', views.Edit_TicketAdminStatus, name='edit_ticketAdminStatus'),
    path('update/ticketAdminStatus/', views.Update_TicketAdminStatus, name='update_ticketAdminStatus'),
    path('delete/ticketAdminStatus/<str:id>', views.Delete_TicketAdminStatus, name='delete_ticketAdminStatus'),

    path('add/feStatus/', views.Add_EFStatus, name='add_FEStatus'),
    path('view/feStatus/', views.View_FEStatus, name='view_FEStatus'),
    path('edit/feStatus/<str:id>', views.Edit_FEStatus, name='edit_FEStatus'),
    path('update/feStatus/', views.Update_FEStatus, name='update_FEStatus'),
    path('delete/feStatus/<str:id>', views.Delete_FEStatus, name='delete_FEStatus'),

    path('add/FEWork/', views.Add_FEWork, name='add_FEWork'),
    path('view/FEWork/', views.View_FEWork, name='view_FEWork'),
    path('edit/FEWork/<str:id>', views.Edit_FEWork, name='edit_FEWork'),
    path('update/FEWork/', views.Update_FEWork, name='update_FEWork'),
    path('delete/FEWork/<str:id>', views.Delete_FEWork, name='delete_FEWork'),

    path('add/workActivity/', views.Add_WorkActivity, name='add_workActivity'),
    path('view/workActivity/', views.View_WorkActivity, name='view_workActivity'),
    path('edit/workActivity/<str:id>', views.Edit_WorkActivity, name='edit_workActivity'),
    path('update/workActivity/', views.Update_WorkActivity, name='update_workActivity'),
    path('delete/workActivity/<str:id>', views.Delete_WorkActivity, name='delete_workActivity'),

    path('add/ticketExternalNotes/', views.Add_TicketExternalNotes, name='add_ticketExternalNotes'),
    path('view/ticketExternalNotes/', views.View_TicketExternalNotes, name='view_ticketExternalNotes'),
    path('edit/ticketExternalNotes/<str:id>', views.Edit_TicketExternalNotes, name='edit_ticketExternalNotes'),
    path('update/ticketExternalNotes/', views.Update_TicketExternalNotes, name='update_ticketExternalNotes'),
    path('delete/ticketExternalNotes/<str:id>', views.Delete_TicketExternalNotes, name='delete_ticketExternalNotes'),

    path('add/ticketInternalNotes/', views.Add_TicketInternalNotes, name='add_ticketInternalNotes'),
    path('view/ticketInternalNotes/', views.View_TicketInternalNotes, name='view_ticketInternalNotes'),
    path('edit/ticketInternalNotes/<str:id>', views.Edit_TicketInternalNotes, name='edit_ticketInternalNotes'),
    path('update/ticketInternalNotes/', views.Update_TicketInternalNotes, name='update_ticketInternalNotes'),
    path('delete/ticketInternalNotes/<str:id>', views.Delete_TicketInternalNotes, name='delete_ticketInternalNotes'),


    path('add/ticketAgainstFE/', views.Add_TicketAgainstFE, name='add_ticketAgaisntFE'),
    # path(),
    # path(),
    # path(),
    # path(),

    path('add/ticketExpense/', views.Add_TicketExpense, name='add_ticketExpense'),
    # path('add/ticketExternalNotes/', views.Add_TicketExternalNotes, name='add_ticketExternalNotes'),
    # path('add/ticketInternalNotes/', views.Add_TicketInternalNotes, name='add_ticketInternalNotes'),
    path('add/ticketActionHistory/', views.Add_TicketActionHistory, name='add_ticketActionHistory'),

    path('add/enggwork', views.Add_EnggWork, name='add_enggwork'),
    path('view/enggwork/', views.View_EnggWork, name='view_enggwork'),

    path('add/country', views.Add_Country, name='add_country'),
    path('view/country/', views.View_Country, name='view_country'),
    path('edit/country/<str:id>', views.Edit_Country, name='edit_country'),
    path('update/country', views.Update_country, name='update_country'),
    path('delete/country/<str:id>', views.Delete_Country, name='delete_country'),

    path('add/city', views.Add_City, name='add_city'),
    path('view/city', views.View_City, name='view_city'),
    path('edit/city/<str:id>', views.Edit_City, name='edit_city'),
    path('update/city/', views.Update_City, name='update_city'),
    path('delete/city/<str:id>', views.Delete_City, name='delete_city'),

    path('load-city', views.load_city, name='ajax_load_city'),
    path('load-end-client', views.load_end_client, name='ajax_load_endclient'),
    path('load-mixup', views.load_clientandcity, name='ajax_load_clientandcity'),

    path('add/customercategory', views.Add_CustomerCategory, name='add_customercategory'),
    path('view/customercategory/', views.View_CustomerCategory, name='view_customercategory'),
    path('edit/customercategory/<str:id>', views.Edit_CustomerCategory, name='edit_customercategory'),
    path('update/customercategory', views.Update_CustomerCategory, name='update_customercategory'),
    path('delete/customercategory/<str:id>', views.Delete_CustomerCategory, name='delete_customercategory'),

    path('add/customertype', views.Add_CustomerType, name='add_customertype'),
    path('view/customertype', views.View_CustomerType, name='view_customertype'),
    path('edit/customertype/<str:id>', views.Edit_CustomerType, name='edit_customertype'),
    path('update/customertype', views.Update_CustomerType, name='update_customertype'),
    path('delete/customertype/<str:id>', views.Delete_CustomerType, name='delete_customertype'),

    path('add/customer', views.Add_Customer, name='add_customer'),
    path('view/customer', views.View_Customer, name='view_customer'),
    path('edit/customer/<str:id>', views.Edit_Customer, name='edit_customer'),
    path('update/customer', views.Update_Customer, name='update_customer'),
    path('delete/customer/<str:id>', views.Delete_Customer, name='delete_customer'),

    path('add/classes', views.Add_Classes, name='add_classes'),
    path('view/classes', views.View_Classes, name='view_classes'),
    path('edit/classes/<str:id>', views.Edit_Classes, name='edit_classes'),
    path('update/classes', views.Update_Classes, name='update_classes'),
    path('delete/classes/<str:id>', views.Delete_Classes, name='delete_classes'),

    path('add/productcategory/', views.Add_ProductCategory, name='add_productcategory'),
    path('view/productcategory/', views.View_ProductCategory, name='view_productcategory'),
    path('edit/productcategory/<str:id>', views.Edit_ProductCategory, name='edit_productcategory'),
    path('update/productcategory/', views.Update_ProductCategory, name='update_productcategory'),
    path('delete/productcategory/<str:id>', views.Delete_ProductCategory, name='delete_productcategory'),



    path('add/options/', views.Add_Options, name='add_options'),
    path('view/options/', views.View_Options, name='view_options'),
    path('edit/options/<str:id>', views.Eidt_Options, name='edit_options'),
    path('update/options/', views.Update_Options, name='update_options'),
    path('delete/options/<str:id>', views.Delete_Options, name='delete_options'),


    path('add/categoryone/', views.Add_CategoryOne, name='add_categoryone'),
    path('view/categoryone/', views.View_CategoryOne, name='view_categoryone'),
    path('edit/categoryone/<str:id>', views.Edit_CategoryOne, name='edit_categoryone'),
    path('update/categoryone/', views.Update_CategoryOne, name='update_categoryone'),
    path('delete/categoryone/<str:id>', views.Delete_CategoryOne, name='delete_categoryone'),

    path('add/categorytwo/', views.Add_CategoryTwo, name='add_categorytwo'),
    path('view/categorytwo/', views.View_CategoryTwo, name='view_categorytwo'),
    path('edit/categorytwo/<str:id>', views.Edit_CategoryTwo, name='edit_categorytwo'),
    path('update/categorytwo/', views.Update_CategoryTwo, name='update_categorytwo'),
    path('delete/categorytwo/<str:id>', views.Delete_CategoryTwo, name='delete_categorytwo'),


    path('add/categorythree/', views.Add_CategoryThree, name='add_categorythree'),
    path('view/categorythree/', views.View_CategoryThree, name='view_categorythree'),
    path('edit/categorythree/<str:id>', views.Edit_CategoryThree, name='edit_categorythree'),
    path('update/categorythree/', views.Update_CategoryThree, name='update_categorythree'),
    path('delete/categorythree/<str:id>', views.Delete_CategoryThree, name='delete_categorythree'),

    path('add/categoryfour/', views.Add_CategoryFour, name='add_categoryfour'),
    path('view/categoryfour/', views.View_CategoryFour, name='view_categoryfour'),
    path('edit/categoryfour/<str:id>', views.Edit_CategoryFour, name='edit_categoryfour'),
    path('update/categoryfour/', views.Update_CategoryFour, name='update_categoryfour'),
    path('delete/categoryfour/<str:id>', views.Delete_CategoryFour, name='delete_categoryfour'),


    path('add/province', views.Add_Province, name='add_province'),
    path('view/province', views.View_Province, name='view_province'),
    path('edit/province/<str:id>', views.Edit_Province, name='edit_province'),
    path('update/province', views.Update_Province, name='update_province'),
    path('delete/province/<str:id>', views.Delete_Province, name='delete_province'),

    path('add/area', views.Add_Area, name='add_area'),
    path('view/area', views.View_Area, name='view_area'),
    path('edit/area/<str:id>', views.Edit_Area, name='edit_area'),
    path('update/area', views.Update_Area, name='update_area'),
    path('delete/area/<str:id>', views.Delete_Area, name='delete_area'),


    path('add/product/', views.Add_Product, name='add_product'),
    path('view/product', views.View_Product, name='view_product'),
    path('edit/product/<str:id>', views.Edit_Product, name='edit_product'),
    path('update/product', views.Update_Product, name='update_product'),
    path('delete/product/<str:id>', views.Delete_Product, name='delete_product'),


    

    path('add/mazdoor/', views.Add_Mazdoor, name='add_mazdoor'),
    path('view/mazdoor', views.View_Mazdoor, name='view_mazdoor'),
    path('edit/mazdoor/<str:id>', views.Edit_Mazdoor, name='edit_mazdoor'),
    path('update/mazdoor', views.Update_Mazdoor, name='update_mazdoor'),
    path('delete/mazdoor/<str:id>', views.Delete_Mazdoor, name='delete_mazdoor'),


    path('add/lot/', views.Add_Lot, name='add_lot'),
    path('view/lot', views.View_Lot, name='view_lot'),
    path('edit/lot/<str:id>', views.Edit_Lot, name='edit_lot'),
    path('update/lot', views.Update_Lot, name='update_lot'),
    path('delete/lot/<str:id>', views.Delete_Lot, name='delete_lot'),

    path('add/warehouse/', views.Add_Warehouse, name='add_warehouse'),
    path('view/warehouse', views.View_Warehouse, name='view_warehouse'),
    path('edit/warehouse/<str:id>', views.Edit_Warehouse, name='edit_warehouse'),
    path('update/warehouse', views.Update_Warehouse, name='update_warehouse'),
    path('delete/warehouse/<str:id>', views.Delete_Warehouse, name='delete_warehouse'),


    path('add/stock/', views.Add_Stock, name='add_stock'),
    path('view/stock', views.View_Stock, name='view_stock'),
    path('edit/stock/<str:id>', views.Edit_Stock, name='edit_stock'),
    path('update/stock', views.Update_Stock, name='update_stock'),
    path('delete/stock/<str:id>', views.Delete_Stock, name='delete_stock'),


    path('add/account/', views.Add_Account, name='add_account'),
    path('view/account', views.View_Account, name='view_account'),
    path('edit/account/<str:id>', views.Edit_Account, name='edit_account'),
    path('update/account', views.Update_Account, name='update_account'),
    path('delete/account/<str:id>', views.Delete_Account, name='delete_account'),

    path('add/transaction/', views.Add_Transaction, name='add_transaction'),
    path('view/transaction', views.View_Transaction, name='view_transaction'),
    path('edit/transaction/<str:id>', views.Edit_Transaction, name='edit_transaction'),
    path('update/transaction', views.Update_Transaction, name='update_transaction'),
    path('delete/transaction/<str:id>', views.Delete_Transaction, name='delete_transaction'),

    path('add/ledgerentry/', views.Add_LedgerEntry, name='add_ledgerentry'),
    path('view/ledgerentry', views.View_LedgerEntry, name='view_ledgerentry'),
    path('edit/ledgerentry/<str:id>', views.Edit_LedgerEntry, name='edit_ledgerentry'),
    path('update/ledgerentry', views.Update_LedgerEntry, name='update_ledgerentry'),
    path('delete/ledgerentry/<str:id>', views.Delete_LedgerEntry, name='delete_ledgerentry'),    





]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
