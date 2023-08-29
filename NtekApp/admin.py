from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type'] 

admin.site.register(CustomUser,UserModel)

admin.site.register(Client)
admin.site.register(ContractStatus)
admin.site.register(ContractSLA)
admin.site.register(ContractType)
admin.site.register(ContractSubType)
admin.site.register(Contract)

admin.site.register(ProjectStatus)
admin.site.register(ProjectType)
admin.site.register(ProjectSubType)
admin.site.register(Project)

admin.site.register(FieldEngineer)

admin.site.register(TicketStatus)
admin.site.register(TicketStatusHistory)
admin.site.register(TicketType)
admin.site.register(TicketSubType)
admin.site.register(Ticket)
admin.site.register(TicketExpenses)
admin.site.register(TicketExternalNotes)
admin.site.register(TicketInternalNotes)
admin.site.register(TicketActionHistory)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(EndClient)
admin.site.register(BillAble)
admin.site.register(TickeAdminStatus)
admin.site.register(Expense)
admin.site.register(CustomerCategory)
admin.site.register(CustomerType)
admin.site.register(Customers)
admin.site.register(Classes)
admin.site.register(ProductCategory)
admin.site.register(Options)
admin.site.register(Province)
admin.site.register(Area)

