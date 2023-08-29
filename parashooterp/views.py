from asyncio.windows_events import NULL
from dataclasses import Field
from datetime import datetime
from itertools import count
from queue import Empty
import re
from tabnanny import check
from django.shortcuts import render, redirect, HttpResponse
from parashooterp import settings
# from NetkErp.settings import DATE_INPUT_FORMATS, DATE_FORMAT
# from NetkErp.NtekApp.forms import EndClientForm 
from parashootapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from parashootapp.models import *
from parashootapp.forms import *
from datetime import datetime




def BASE(request):
    return render(request, 'base.html')

def LOGIN(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                return HttpResponse('This is Engineer Panel')
            else:
                messages.error(request,'Email or Password are invalid!!!')
                return redirect('login')
        else:
            #message import from django message framework
            messages.error(request,'Email or Password are invalid!!!')
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context ={
        "user":user,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, "your profile Updated Successfully!") 
        except:
            messages.error(request, "Failed to Update your profile")
    return render(request, 'profile.html')

def load_city(request):
    country = request.GET.get('country')
    city = City.objects.filter(Country=country).order_by('CityName')
    context = {
        'city':city,
    }
    return render(request, 'City/city_dropdown_list_options.html', context)

def load_end_client(request):
    client = request.GET.get('client')
    endclient = EndClient.objects.filter(client=client).order_by('CompanyName')
    context = {
        'endclient':endclient
    }
    return render(request, 'EndClient/endclient_dropdown_list.html', context)

def load_clientandcity(request):
    country = request.GET.get('country')
    city = City.objects.filter(Country=country).order_by('CityName')

    client = request.GET.get('client')
    endclient = EndClient.objects.filter(client=client).order_by('CompanyName')
    
    context = {
        'city':city,
        'endclient':endclient,
    }
    return render(request, 'Ticket/endclient_city_dropdown_list.html', context)

def Add_Company(request):
    country = Country.objects.all()
    city = City.objects.all()

    if request.method == "POST":
        CompanyName = request.POST.get('CompanyName')
        Address1 = request.POST.get('Address1')
        Address2 = request.POST.get('Address2')

        country_id = request.POST.get('country_id')
        city_id = request.POST.get('city_id')

        country = Country.objects.get(CountryID=country_id)
        city = City.objects.get(CityID=city_id)
       
        company = Client(
            CompanyName = CompanyName,
            Address1 = Address1,
            Address2 = Address2,
            Country = country,
            City = city,

        ) 
        company.save()
        messages.success(request, company.CompanyName + " saved successfully")
        return redirect('view_company')
    context = {
            'country':country,
            'city':city,
        }

    return render(request, "Company/add_company.html", context)

def View_Company(request):
    company = Client.objects.all()
    context = {
        'company':company
    }
    return render(request, 'Company/view_company.html', context)

def Edit_Company(request, id):
    company = Client.objects.get(ClientID=id)
    country = Country.objects.all()
    city = City.objects.all()
    context = {
        'company':company,
        'country':country,
        'city':city,
    }
    return render(request, 'Company/edit_company.html', context)

def Update_Company(request):
    if request.method == "POST":

        client_id = request.POST.get('client_id')
        CompanyName = request.POST.get('CompanyName')
        Address1 = request.POST.get('Address1')
        Address2 = request.POST.get('Address2')

        city_id = request.POST.get('city_id')
        country_id = request.POST.get('country_id')


        client = Client.objects.get(ClientID=client_id)
        city = City.objects.get(CityID=city_id)
        country = Country.objects.get(CountryID=country_id)

        client.CompanyName = CompanyName
        client.Address1 = Address1
        client.Address2 = Address2
        client.City = city
        client.Country = country
        client.save()
        messages.success(request, "Record Updated Successfully")
        return redirect('view_company')
    return render(request, 'Company/view_company.html')

def Delete_Company(request, id):
    company = Client.objects.get(ClientID=id)
    company.delete()
    messages.success(request, 'Record are successfully deleted!')
    return redirect('view_company')

def Add_EndCompany(request):
    clientt = Client.objects.all()
    country = Country.objects.all()
    city = City.objects.all()
    if request.method == "POST":
        client_id = request.POST.get('client_id')
        CompanyName = request.POST.get('CompanyName')
        Address1 = request.POST.get('Address1')
        Address2 = request.POST.get('Address2')

        country_id = request.POST.get('country_id')
        city_id = request.POST.get('city_id')

        client = Client.objects.get(ClientID=client_id)
        country = Country.objects.get(CountryID=country_id)
        city = City.objects.get(CityID=city_id)
        endcilent = EndClient(
            CompanyName = CompanyName,
            Address1 = Address1,
            Address2 = Address2,
            client = client,
            Country = country,
            City = city,
            
        )
        endcilent.save()
        messages.success(request, 'Vendor / End-Client has been saved successfully!')
        return redirect('view_endcompany')
        
    context = {
        'clientt':clientt,
        'country':country,
        'city':city,
    }
    return render(request, 'EndClient/add_endcompany.html', context)

def View_EndCompany(request):
    company = EndClient.objects.all()
    context = {
        'company':company,
    }
    return render(request, 'EndClient/view_endcompany.html', context)

def Edit_EndCompany(request, id):
    endclient = EndClient.objects.get(EndClientID=id)
    company = Client.objects.all()
    country = Country.objects.all()
    city = City.objects.all()
    context = {
        'endclient':endclient,
        'company':company,
        'country':country,
        'city':city,
    }
    return render(request, 'EndClient/edit_endcompany.html', context)

def Update_EndCompany(request):
    if request.method == "POST":

        endclient_id = request.POST.get('endclient_id')
        CompanyName = request.POST.get('CompanyName')
        Address1 = request.POST.get('Address1')
        Address2 = request.POST.get('Address2')

        client_id = request.POST.get('client_id')
        city_id = request.POST.get('city_id')
        country_id = request.POST.get('country_id')
        

        client = Client.objects.get(ClientID=client_id)
        city = City.objects.get(CityID=city_id)
        country = Country.objects.get(CountryID=country_id)
        endclient = EndClient.objects.get(EndClientID=endclient_id)

        endclient.CompanyName = CompanyName
        endclient.client = client
        endclient.Address1 = Address1
        endclient.Address2 = Address2

        endclient.City = city
        endclient.Country = country
        endclient.save()

        messages.success(request, "Record Updated Successfully")
        return redirect('view_endcompany')
    return render(request, 'EndClient/view_endcompany.html')

def Delete_EndCompany(request, id):
    endcompany = EndClient.objects.get(EndClientID=id)
    endcompany.delete()
    messages.success(request, 'Record are successfully deleted!')
    return redirect('view_endcompany')

# field engineer 

def Add_Engg(request):
    country = Country.objects.all()
    city = City.objects.all()
    if request.method == "POST":
        EmpID = request.POST.get('EmpID')
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')

        country_id = request.POST.get('country_id')
        city_id = request.POST.get('city_id')

        Email = request.POST.get('Email')
        Mobile = request.POST.get('Mobile')

        country = Country.objects.get(CountryID=country_id)
        city = City.objects.get(CityID=city_id)

        engg = FieldEngineer(
            EmployeeID = EmpID,
            FirstName = FirstName,
            LastName = LastName,
            Country = country,
            City = city,
            Email = Email,
            Mobile = Mobile,
        )
        engg.save()
        messages.success(request, 'Field Engineer Has Been Saved Successfully')
        return redirect('view_engg')
    context = {
        'country':country,
        'city':city,
    }
    return render(request, 'Engineer/add_engg.html', context)

def View_Engg(request):
    engineer = FieldEngineer.objects.all()
    context = {
        'engineer':engineer
    }
    return render(request, 'Engineer/view_engg.html', context)

def Edit_Engg(request, id):
    engineer = FieldEngineer.objects.get(FEID=id)
    country = Country.objects.all()
    city = City.objects.all()
    context = {
        "engineer":engineer,
        "country":country,
        "city":city,
    }
    return render(request, 'Engineer/edit_engg.html', context)

def Update_Engg(request):
    if request.method == "POST":
        emp_id = request.POST.get('emp_id')
        engg_id = request.POST.get('engg_id')
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        country_id = request.POST.get('country_id')
        city_id = request.POST.get('city_id')
        Email = request.POST.get('Email')
        Mobile = request.POST.get('Mobile')

        engg = FieldEngineer.objects.get(FEID=engg_id)
        country = Country.objects.get(CountryID=country_id)
        city = City.objects.get(CityID=city_id)

        engg.EmployeeID = emp_id
        engg.FirstName = FirstName
        engg.LastName = LastName
        engg.Country = country
        engg.City = city
        engg.Email = Email
        engg.Mobile = Mobile
        engg.save()

        messages.success(request, 'Field Engineer Has Been Updated Successfully')
        return redirect('view_engg')
    return render(request, 'Engineer/view_engg.html')

def Delete_Engg(request, id):
    engineer = FieldEngineer.objects.get(FEID=id)
    engineer.delete()
    messages.success(request, 'Record Deleted Successfully!')
    return redirect('view_engg')


def Add_ContractSLA(request):
    if request.method == "POST":
        contractsla = request.POST.get('contractsla')
        csla = ContractSLA(
            ContractSLA = contractsla,
        )
        csla.save()
        messages.success(request, "Contract-SLA, has been saved!")
        return redirect('view_contractSLA')

    return render(request, 'Contract/add_contractSLA.html')

def View_ContractSLA(request):
    csla = ContractSLA.objects.all()
    context = {
        'csla':csla,
    }
    return render(request, 'Contract/view_contractSLA.html', context)

def Edit_ContractSLA(request, id):
    sla = ContractSLA.objects.get(SLAID=id)
    context = {
        'sla':sla,
    }
    return render(request, 'Contract/edit_contractSLA.html', context)

def Update_ContractSLA(request):
    if request.method == "POST":
        contractSLA_id = request.POST.get('contractSLA_id')
        contractSLA_name = request.POST.get('contractSLA_name')

        contractSLA = ContractSLA.objects.get(SLAID=contractSLA_id)
        contractSLA.ContractSLA = contractSLA_name
        contractSLA.save()

        messages.success(request, 'Contract-SLA has been updated successfully')
        return redirect('view_contractSLA')
    return render(request, 'Contract/view_contractSLA.html')

def Delete_ContractSLA(request, id):
    contractSLA = ContractSLA.objects.get(SLAID=id)
    contractSLA.delete()
    messages.success(request, 'Contract-SLA has been deleted successfully')
    return redirect('view_contractSLA')
    
def Add_ContractType(request):
    if request.method == "POST":
        contracttype = request.POST.get('contracttype')
        cont = ContractType(
            ContractType = contracttype
        )
        cont.save()
        messages.success(request, 'Contract Type Has been Added Successfully')
        return redirect('view_contractType')
    return render(request, 'Contract/add_contractType.html')

def View_ContractType(request):
    contype = ContractType.objects.all()
    context = {
        'contype':contype,
    }
    return render(request, 'Contract/view_contractType.html', context)

def Edit_ContractType(request, id):
    contype = ContractType.objects.get(CTID=id)
    context = {
        'contype':contype
    }
    return render(request, 'Contract/edit_contractType.html', context)

def Update_ContractType(request):
    if request.method == "POST":
        contracttype_id = request.POST.get('contracttype_id')
        contracttype_name = request.POST.get('contracttype_name')
        contype = ContractType.objects.get(CTID=contracttype_id)
        contype.ContractType = contracttype_name
        contype.save()
        messages.success(request, "Contract Type has been updated!")
        return redirect('view_contractType')
    return render(request, 'Contract/view_contractType.html')

def Delete_ContractType(request, id):
    contype = ContractType.objects.get(CTID=id)
    contype.delete()
    messages.success(request, 'Contract Type has been deleted successfully!')
    return redirect('view_contractType')


def Add_ContractSubType(request):
    contype = ContractType.objects.all()
    if request.method == "POST":
        contractType_id = request.POST.get('contractType_id')
        cont_subtype = request.POST.get('cont_subtype')
        contractype = ContractType.objects.get(CTID=contractType_id)
        contsubtype = ContractSubType(
            ContractSubType = cont_subtype,
            ContratctType =  contractype
        )
        contsubtype.save()
        messages.success(request, 'Contract Sub Type has been added successfully!')
        return redirect('view_contractSubType')
    context = {
        'contype':contype,
    }
    return render(request, 'Contract/add_contractSubType.html', context)

def View_ContractSubType(request):
    contractsubtype = ContractSubType.objects.all()
    context = {
        'contractsubtype':contractsubtype,
    }
    return render(request, 'Contract/view_contractSubType.html', context)

def Edit_ContractSubType(request, id):
    contractsubtype = ContractSubType.objects.get(CSTID=id)

    id = request.GET.get('id')
    contracttype = ContractType.objects.filter(CTID=id).order_by('ContractType')
    context = {
        'contractsubtype':contractsubtype,
        'contracttype':contracttype,
    }
    return render(request, 'Contract/edit_contractSubType.html', context)

def Update_ContractSubType(request):
    if request.method == "POST":
        contractType_id = request.POST.get('contractType_id')
        cont_subtype_id = request.POST.get('cont_subtype_id')
        cont_subtype = request.POST.get('cont_subtype')

        contractype = ContractType.objects.get(CTID=contractType_id)
        contractsubtype = ContractSubType.objects.get(CSTID=cont_subtype_id)

        contractsubtype.ContractSubType = cont_subtype
        contractsubtype.ContratctType = contractype
        contractsubtype.save()
        messages.success(request, 'Contract Sub Type has been updated successfully!')
        return redirect('view_contractSubType')

    return render(request, 'Contract/view_contractSubType.html')

def Delete_ContractSubType(request, id):
    consutype = ContractSubType.objects.get(CSTID=id)
    consutype.delete()
    messages.success(request, 'Contract Sub Type has been deleted!')
    return redirect('view_contractSubType')

def Add_ContractStatus(request):
    if request.method == "POST":
        contractstatus = request.POST.get('contractstatus')
        constatus = ContractStatus(
            ContractStatus = contractstatus,
        )
        constatus.save()
        messages.success(request, 'Status has been saved successfully!')
        return redirect('view_contractStatus')
    return render(request, 'Contract/add_contractStatus.html')

def View_ContractStatus(request):
    contatsu = ContractStatus.objects.all()
    context = {
        'contatsu':contatsu,
    }
    return render(request, 'Contract/view_contractStatus.html', context)

def Edit_ContractStatus(request, id):
    contrctst = ContractStatus.objects.get(CSID=id)
    context = {
        'contrctst':contrctst,
    }
    return render(request, 'Contract/edit_contractStatus.html', context)

def Update_ContractStatus(request):
    if request.method == "POST":
        contractstatus_id = request.POST.get('contractstatus_id')
        contractstatus_name = request.POST.get('contractstatus_name')

        cstatus = ContractStatus.objects.get(CSID=contractstatus_id)
        cstatus.ContractStatus = contractstatus_name
        cstatus.save()
        messages.success(request, 'Contract has been updated successfully!')
        return redirect('view_contractStatus')

    return render(request, 'Contract/view_contractStatus.html')

def Delete_ContractStatus(request, id):
    costatus = ContractStatus.objects.get(CSID=id)
    costatus.delete()
    messages.success(request, 'Contract has been deleted successfully!')
    return redirect('view_contractStatus')

def Add_Contract(request):
    client = Client.objects.all()
    contype = ContractType.objects.all()
    endclient = EndClient.objects.all()
    contSLA = ContractSLA.objects.all()
    CStatus = ContractStatus.objects.all()
    # date_string = DATETIME_FORMAT

    if request.method == "POST":
        contractno = request.POST.get('contractno')
        contractname = request.POST.get('contractname')
        clientrn = request.POST.get('clientrn')
        description = request.POST.get('description')
        client_id = request.POST.get('client_id')
        endclient_id = request.POST.get('endclient_id')

        # startdate = request.POST.get('startdate')
        # enddate = request.POST.get('enddate')

        startdate = datetime.strptime(request.POST['startdate'], '%d:%m:%Y')
        enddate = datetime.strptime(request.POST['enddate'], '%d:%m:%Y')

        # start_date = datetime.strptime(startdate, '%d-%m-%y %H:%M:%S.%f').strftime('%Y-%m-%d')
        # end_date = datetime.strptime(enddate, '%d-%m-%y %H:%M:%S.%f').strftime('%Y-%m-%d')

        # startdate = request.POST.get('startdate').datetime.datetime.strptime('%d-%m-%y').strftime('%Y-%m-%d')
        # enddate = request.POST.get('enddate').datetime.datetime.strptime('%d-%m-%y').strftime('%Y-%m-%d')

        # startdate = request.POST.get(datetime.strptime('date_string', '%d-%m-%y').strftime('%Y-%m-%d'))
        # enddate = request.POST.get(datetime.strptime('date_string', '%d-%m-%y').strftime('%Y-%m-%d'))

        contractType_id = request.POST.get('contractType_id')
        contractSLA_id = request.POST.get('contractSLA_id')
        contractStatus_id = request.POST.get('contractStatus_id')

        clients = Client.objects.get(ClientID=client_id)
        contracttype = ContractType.objects.get(CTID=contractType_id)
        endclients = EndClient.objects.get(EndClientID=endclient_id)
        cotractsla = ContractSLA.objects.get(SLAID=contractSLA_id)
        contractstatus = ContractStatus.objects.get(CSID=contractStatus_id)

        contract = Contract(
            ContractNo = contractno,
            ContractName = contractname,
            ClientRefNo = clientrn,
            Description = description,
            Client = clients,
            StartDate = startdate,
            EndDate = enddate,
            ContractType = contracttype,
            EndClient = endclients,
            ContractSLA = cotractsla,
            CStatus = contractstatus,
        )
        contract.save()
        messages.success(request, 'Contract Has been save successfully!')
        return redirect('view_contract')

    context = {
        'client':client,
        'contype':contype,
        # 'contsubype':contsubype,
        'endclient':endclient,
        'contSLA':contSLA,
        'CStatus':CStatus,
    }
        
    return render(request, 'Contract/add_contract.html', context)

def View_Contract(request):
    contract = Contract.objects.all()
    context = {
        'contract':contract,
    }
    return render(request, 'Contract/view_contract.html', context)

def Edit_Contract(request, id):
    contract = Contract.objects.get(ContractID=id)
    client = Client.objects.all()
    ctype = ContractType.objects.all()
    # cstype = ContractSubType.objects.all()
    endclient = EndClient.objects.all()
    csla = ContractSLA.objects.all()
    CStatus = ContractStatus.objects.all()
    context = {
        'contract':contract,
        'client':client,
        'ctype':ctype,
        # 'cstype':cstype,
        'endclient':endclient,
        'csla':csla,
        'CStatus':CStatus,
    }
    return render(request, 'Contract/edit_contract.html', context)

def Update_Contract(request):
    if request.method == "POST":
        contract_id = request.POST.get('contract_id')
        contract_no = request.POST.get('contract_no')
        contract_name = request.POST.get('contract_name')
        client_rn = request.POST.get('client_rn')
        description = request.POST.get('description')
        client_id = request.POST.get('client_id')
        endclient_id = request.POST.get('endclient_id')

        # startdate = request.POST.get('startdate')
        # enddate = request.POST.get('enddate')

        startdate = datetime.strptime(request.POST['startdate'], '%d:%m:%Y')
        enddate = datetime.strptime(request.POST['enddate'], '%d:%m:%Y')

        contractType_id = request.POST.get('contractType_id')
        # contsubtype_id = request.POST.get('contsubtype_id')
        contractSLA_id = request.POST.get('contractSLA_id')
        contractStatus_id = request.POST.get('contractStatus_id')

        client = Client.objects.get(ClientID=client_id)
        endclient = EndClient.objects.get(EndClientID=endclient_id)
        contracttype = ContractType.objects.get(CTID=contractType_id)
        # consubtype = ContractSubType.objects.get(CSTID=contsubtype_id)
        contractsla = ContractSLA.objects.get(SLAID=contractSLA_id)
        contractstatus = ContractStatus.objects.get(CSID=contractStatus_id)

        contract = Contract(
            ContractID = contract_id,
            ContractNo = contract_no,
            ContractName = contract_name,
            ClientRefNo = client_rn,
            Description = description,
            StartDate = startdate,
            EndDate = enddate,
            Client = client,
            EndClient = endclient,
            ContractType = contracttype,
            # ContractSubType = consubtype,
            ContractSLA = contractsla,
            CStatus = contractstatus
        )
        contract.save()
        messages.success(request, 'Contract has been updated successfully')
        return redirect('view_contract')

    return render(request, 'Contract/view_contract.html')

def Delete_Contract(request, id):
    contract = Contract.objects.get(ContractID=id)
    contract.delete()
    messages.success(request, "Contract has been deleted successfully!")
    return redirect('view_contract')

#project

def Add_ProjectType(request):
    if request.method == "POST":
        project_type = request.POST.get('project_type')
        ptype = ProjectType(
        ProjectType = project_type
        )
        ptype.save()
        messages.success(request, 'Project Type Has been Added Successfully')
        return redirect('view_projectType')
    return render(request, 'Projects/ProjectType/add_projectType.html')

def View_ProjectType(request):
    ptype = ProjectType.objects.all()
    context = {
        'ptype':ptype,
    }
    return render(request, 'Projects/ProjectType/view_projectType.html', context)

def Edit_ProjectType(request, id):
    typep = ProjectType.objects.get(PTID=id)
    context = {
        'typep':typep,
    }
    return render(request, 'Projects/ProjectType/edit_projectType.html', context)

def Update_ProjectType(request):
    if request.method == "POST":
        projectType_id = request.POST.get('projectType_id')
        Project_type = request.POST.get('Project_type')
        protype = ProjectType.objects.get(PTID=projectType_id)
        protype.ProjectType = Project_type
        protype.save()
        messages.success(request, 'Project Type has been updated successfully!')
        return redirect('view_projectType')
    return render(request, 'Projects/ProjectType/view_projectType.html')

def Delete_ProjectType(request, id):
    protype = ProjectType.objects.get(PTID=id)
    protype.delete()
    messages.success(request, 'Project Type has been deleted')
    return redirect('view_projectType')
    
def Add_ProjectSubType(request):
    proty = ProjectType.objects.all()
    if request.method == "POST":
        projectype_id = request.POST.get('projectype_id')
        prosub_type = request.POST.get('prosub_type')

        prtype = ProjectType.objects.get(PTID=projectype_id)
        prsubty = ProjectSubType(
            ProjectSubType = prosub_type,
            ProjectType = prtype,
        )
        prsubty.save()
        messages.success(request, 'Project Sub Type has been Saved Successfully')
        return redirect('view_projectSubType')
    context = {
        'proty':proty
    }
    return render(request, 'Projects/ProjectSubType/add_projectSubType.html', context)

def View_ProjectSubType(request):
    prosubty = ProjectSubType.objects.all()
    context = {
        'prosubty':prosubty
    }
    return render(request, 'Projects/ProjectSubType/view_projectSubType.html', context)



def Edit_ProjectSubType(request, id):
    return render(request, 'Projects/ProjectSubType/edit_projectSubType.html')

def Add_ProjectStatus(request):
    if request.method == "POST":
        project_status = request.POST.get('project_status')
        prostatus = ProjectStatus(
            ProjectStatus = project_status
        )
        prostatus.save()
        messages.success(request, "Project Status has been saved successfully!")
        return redirect('view_projectStatus')
    return render(request, 'Projects/ProjectStatus/add_projectStatus.html')

def View_ProjectStatus(request):
    pstatus = ProjectStatus.objects.all()
    context = {
        'pstatus':pstatus,
    }
    return render(request, 'Projects/ProjectStatus/view_projectStatus.html', context)

def Edit_ProjectStatus(request, id):
    pstatus = ProjectStatus.objects.get(PSID=id)
    context = {
        'pstatus':pstatus,
    }
    return render(request, 'Projects/ProjectStatus/edit_projectStatus.html', context)

def Update_ProjectStauts(request):
    if request.method == "POST":
        projectstatus_id = request.POST.get('projectstatus_id')
        project_status = request.POST.get('project_status')
        prostatus = ProjectStatus.objects.get(PSID=projectstatus_id)
        prostatus.ProjectStatus = project_status
        prostatus.save()
        messages.success(request, "Project Status has been updated successfully!")
        return redirect('view_projectStatus')
    return render(request, 'Projects/ProjectStatus/view_projectStatus.html')

def Delete_ProjectStatus(request, id):
    pstatus = ProjectStatus.objects.get(PSID=id)
    pstatus.delete()
    messages.success(request, "Project Status has been deleted successfully!")
    return redirect('view_projectStatus')

def Add_Project(request):
    client = Client.objects.all()
    ptype = ProjectType.objects.all()
    endclient = EndClient.objects.all()
    pstatus = ProjectStatus.objects.all()

    if request.method == "POST":
        project_name = request.POST.get('project_name')
        client_rn = request.POST.get('client_rn')
        description = request.POST.get('description')
        client_id = request.POST.get('client_id')
        endclient_id = request.POST.get('endclient_id')

        # startdate = request.POST.get('startdate')
        # enddate = request.POST.get('enddate')

        startdate = datetime.strptime(request.POST['startdate'], '%d:%m:%Y')
        enddate = datetime.strptime(request.POST['enddate'], '%d:%m:%Y')

        projectType_id = request.POST.get('projectType_id')
        projectStatus_id = request.POST.get('projectStatus_id')

        clients = Client.objects.get(ClientID=client_id)
        projecttype = ProjectType.objects.get(PTID=projectType_id)
        endclients = EndClient.objects.get(EndClientID=endclient_id)
        projectstatus = ProjectStatus.objects.get(PSID=projectStatus_id)

        project = Project(
            ProjectName = project_name,
            ClientRefNo = client_rn,
            Description = description,
            Client = clients,
            StartDate = startdate,
            EndDate = enddate,
            ProjectType = projecttype,
            EndClient = endclients,
            ProjectStauts = projectstatus,
        )
        project.save()
        messages.success(request, 'Project Has been save successfully!')
        return redirect('view_project')

    context = {
        'client':client,
        'ptype':ptype,
        'endclient':endclient,
        'pstatus':pstatus,
    }
    return render(request, 'Projects/Project/add_project.html', context)

def View_Project(request):
    project = Project.objects.all()
    context = {
        'project':project,
    }
    return render(request, 'Projects/Project/view_project.html', context)

def Edit_Project(request, id):
    project = Project.objects.get(ProjectID=id)
    client = Client.objects.all()
    endclient = EndClient.objects.all()
    ptype = ProjectType.objects.all()
    pstatus = ProjectStatus.objects.all()
    context = {
        'project':project,
        'client':client,
        'endclient':endclient,
        'ptype':ptype,
        'pstatus':pstatus,
    }
    return render(request, 'Projects/Project/edit_project.html', context)

def Update_Project(request):
    if request.method == "POST":
        project_id = request.POST.get('project_id')
        project_name = request.POST.get('project_name')
        client_rn = request.POST.get('client_rn')
        description = request.POST.get('description')
        client_id = request.POST.get('client_id')
        endclient_id = request.POST.get('endclient_id')

        # startdate = request.POST.get('startdate')
        # enddate = request.POST.get('enddate')

        startdate = datetime.strptime(request.POST['startdate'], '%d:%m:%Y')
        enddate = datetime.strptime(request.POST['enddate'], '%d:%m:%Y')

        projectType_id = request.POST.get('projectType_id')
        projectStatus_id = request.POST.get('projectStatus_id')
        
        client = Client.objects.get(ClientID=client_id)
        endclient = EndClient.objects.get(EndClientID=endclient_id)
        projecttype = ProjectType.objects.get(PTID=projectType_id)
        projectstatus = ProjectStatus.objects.get(PSID=projectStatus_id)
        
        project = Project(
            ProjectID = project_id,
            ProjectName = project_name,
            ClientRefNo = client_rn,
            Description = description,
            StartDate = startdate,
            EndDate = enddate,
            Client = client,
            EndClient = endclient,
            ProjectType = projecttype,
            ProjectStauts = projectstatus,
        )
        project.save()
        messages.success(request, 'Project has been updated successfully')
        return redirect('view_project')
    return render(request, 'Projects/Project/view_project.html')

def Delete_Project(request, id ):
    project = Project.objects.get(ProjectID=id)
    project.delete()
    messages.success(request, "Project has been deleted successfully!")
    return redirect('view_project')

def Add_TicketStatus(request):
    if request.method == "POST":
        ticketstatus = request.POST.get('ticketstatus')
        tstatus = TicketStatus(
            TicketStatus = ticketstatus
        )
        tstatus.save()
        messages.success(request, "Ticket Status has been saved successfully!")
        return redirect('view_ticketStatus')
    return render(request, 'Ticket/TicketStatus/add_ticketStatus.html')

def View_TicketStatus(request):
    ticketstatus = TicketStatus.objects.all()
    context = {
        'ticketstatus':ticketstatus,
    }
    return render(request, 'Ticket/TicketStatus/view_ticketStatus.html', context)

def Edit_TicketStatus(request, id):
    ticketstatus = TicketStatus.objects.get(TSID=id)
    context = {
        'ticketstatus':ticketstatus,
    }
    return render(request, 'Ticket/TicketStatus/edit_ticketStatus.html', context)

def Update_TicketStatus(request):
    if request.method == "POST":
        ticketstatus_id = request.POST.get('ticketstatus_id')
        ticketstatus = request.POST.get('ticketstatus')
        tstatus = TicketStatus.objects.get(TSID=ticketstatus_id)
        tstatus.TicketStatus = ticketstatus
        tstatus.save()
        messages.success(request, 'Ticket Status has been updated successfully')
        return redirect('view_ticketStatus')
    return render(request, 'Ticket/TicketStatus/view_ticketStatus.html')

def Delete_TicketStatus(request, id):
    ticketstatus = TicketStatus.objects.get(TSID=id)
    ticketstatus.delete()
    messages.success(request, 'Ticket status has been deleted successfully!')
    return redirect('view_ticketStatus')

def Add_TicketStatusHis(request):
    return render(request, 'Ticket/add_ticketStatusHis.html')

def Add_TicketType(request):
    if request.method == "POST":
        tickettype = request.POST.get('tickettype')
        tiktype = TicketType(
            TicketType = tickettype
        )
        tiktype.save()
        messages.success(request, 'Ticket Type has been saved successfully!')
        return redirect('view_ticketType')
    return render(request, 'Ticket/TicketType/add_ticketType.html')

def View_TicketType(request):
    ticketype = TicketType.objects.all()
    context = {
        'ticketype':ticketype,
    }
    return render(request, 'Ticket/TicketType/view_ticketType.html', context)

def Edit_TicketType(request, id):
    tickettype = TicketType.objects.get(TTID=id)
    context = {
        'tickettype':tickettype,
    }
    return render(request, 'Ticket/TicketType/edit_ticketType.html', context)

def Update_TicketType(request):
    if request.method == "POST":
        tickettype_id = request.POST.get('tickettype_id')
        tickettype = request.POST.get('tickettype')
        ticketype = TicketType.objects.get(TTID=tickettype_id)
        ticketype.TicketType = tickettype
        ticketype.save()
        messages.success(request, 'Ticket Type has been updated successfully!')
        return redirect('view_ticketType')
    return render(request, 'Ticket/TicketType/view_ticketType.html')

def Delete_TicketType(request, id):
    ticketype = TicketType.objects.get(TTID=id)
    ticketype.delete()
    messages.success(request, 'Ticket Type has been deleted successfully!')
    return redirect('view_ticketType')

def Add_TicketSubType(request):
    return render(request, 'Ticket/add_ticketSubType.html')

def Add_Ticket(request):
    contract = Contract.objects.all()
    project = Project.objects.all()
    tickettype = TicketType.objects.all()
    pticketno = Ticket.objects.all()
    billable = BillAble.objects.all()
    client = Client.objects.all()
    endclient = EndClient.objects.all()
    country = Country.objects.all()
    city = City.objects.all()
    if request.method == "POST":
        contract_id = request.POST.get('contract_id')
        project_id = request.POST.get('project_id')
        tickettype_id = request.POST.get('tickettype_id')
        billable_id = request.POST.get('billable_id')
        # parentticket_id = request.POST.get('parentticket_id')
        client_id = request.POST.get('client_id')
        endclient_id = request.POST.get('endclient_id')
        country_id = request.POST.get('country_id')
        city_id = request.POST.get('city_id')
        ticektsch_date = datetime.strptime(request.POST['ticektsch_date'], '%d:%m:%Y %H:%M')
        ticketcom_date = None

        # if request.GET == '':
        #     ticketcom_date = None
        # else:
        #     ticketcom_date = datetime.strptime(request.POST['ticketcom_date'], '%d:%m:%Y %H:%M')

        # ticketcom_date = datetime.strptime(request.POST['ticketcom_date'], '%d:%m:%Y %H:%M')
        
        # if ticketcom_date == "" or ticketcom_date == Empty:
        #     ticketcom_date = None
        # else:
        #     ticketcom_date = datetime.strptime(request.POST['ticketcom_date'], '%d:%m:%Y %H:%M')
            
        # if ticketcom_date == "":
        #     ticketcom_date = None

        # ticketcom_date = datetime.now()
        # if ticketcom_date in request.POST == "":
        #     ticketcom_date = None
        # else:
        #     ticketcom_date = datetime.strptime(request.POST['ticketcom_date'], '%d:%m:%Y')

        subject = request.POST.get('subject')
        reference_no = request.POST.get('reference_no')

        if contract_id == "select":
            contractmod = None
        else:
            contractmod = Contract.objects.get(ContractID=contract_id)

        if project_id == "select":
            projectmod = None
        else:
            projectmod = Project.objects.get(ProjectID=project_id)

        
        tickettypemod = TicketType.objects.get(TTID=tickettype_id)
        bilablemod = BillAble.objects.get(BAID=billable_id)
        # parentticketmod = Ticket.objects.get(TicketID=parentticket_id)
        clientmod = Client.objects.get(ClientID=client_id)
        endclientmod = EndClient.objects.get(EndClientID=endclient_id)
        countrymod = Country.objects.get(CountryID=country_id)
        citymod = City.objects.get(CityID=city_id)

        ticket = Ticket(
            TicketScheduleDate = ticektsch_date,
            TicketCompletedDate = ticketcom_date,
            Subject = subject,
            ReferenceNo = reference_no,
            Contract = contractmod,
            Project = projectmod,
            TicketType = tickettypemod,
            Billable = bilablemod,
            # ParentTicketNo = parentticketmod,
            Client = clientmod,
            EndClient = endclientmod,
            Country = countrymod,
            City = citymod,           
        )
        ticket.save()
        messages.success(request, "Ticket has been saved successfully")
        return redirect('view_ticket')
        

    context ={
        'contract':contract,
        'project':project,
        'tickettype':tickettype,
        'pticketno':pticketno,
        'billable':billable,
        'client':client,
        'endclient':endclient,
        'country':country,
        'city':city,
    }
    return render(request, 'Ticket/add_ticket.html', context)

def View_Ticket(request):
    ticket = Ticket.objects.all()
    context = {
        'ticket':ticket,
    }
    return render(request, 'Ticket/view_ticket.html', context)

def Edit_Ticket(request, id):
    ticket = Ticket.objects.get(TID=id)
    contract = Contract.objects.all()
    project = Project.objects.all()
    tickettype = TicketType.objects.all()
    billable = BillAble.objects.all()
    client = Client.objects.all()
    endclient = EndClient.objects.all()
    country = Country.objects.all()
    city = City.objects.all()
    context = {
        'ticket':ticket,
        'contract':contract,
        'project':project,
        'tickettype':tickettype,
        'billable':billable,
        'client':client,
        'endclient':endclient,
        'country':country,
        'city':city,
    }
    return render(request, 'Ticket/edit_ticket.html', context)


# def Add_TicketAdminStatus(request):
    if request.method == "POST":
        opencheck = request.POST.get('opencheck')
        schedulecheck = request.POST.get('schedulecheck')
        closedcheck = request.POST.get('closedcheck')
        onholdcheck = request.POST.get('onholdcheck')
        canceledcheck = request.POST.get('canceledcheck')

        if request.GET:
            OpenCheckDescp = datetime.strptime(request.POST['OpenCheckDescp'], '%d:%m:%Y %H:%M')
        else:
            OpenCheckDescp = None
            

        if request.GET:
            SchCheckDescp = datetime.strptime(request.POST['SchCheckDescp'], '%d:%m:%Y %H:%M')
        else:
            SchCheckDescp = None
            

        if request.GET:
            CloCheckDescp = datetime.strptime(request.POST['CloCheckDescp'], '%d:%m:%Y %H:%M')
        else:
            CloCheckDescp = None
            

        if request.GET:
            OnHoldCheckDescp = datetime.strptime(request.POST['OnHoldCheckDescp'], '%d:%m:%Y %H:%M')
        else:
            OnHoldCheckDescp = None
            

        if request.GET:
            CancelCheckDescp = datetime.strptime(request.POST['CancelCheckDescp'], '%d:%m:%Y %H:%M')
        else:
            CancelCheckDescp = None
            

        

        ticketas = TickeAdminStatus(
            TicketOpen = opencheck,
            TicketSchedule = schedulecheck,
            TicketClosed = closedcheck,
            TicketOnHold = onholdcheck,
            TicketCanceled = canceledcheck,

            OpenTime = OpenCheckDescp,           
            ScheduleTime = SchCheckDescp,           
            ClosedTime = CloCheckDescp,           
            OnHoldTime = OnHoldCheckDescp,           
            CancelledTime = CancelCheckDescp,
        )
        ticketas.save()
        messages.success(request, "Ticekt Admin Status has been saved successfully")
        return redirect('view_ticket')
    return render(request, 'Ticket/add_ticket.html')

def Add_TicketAdminStatus(request):
    ticket = Ticket.objects.all()
    ticketstatus = TicketStatus.objects.all()
    if request.method == "POST":
        ticket_id = request.POST.get('ticket_id')
        ticketstatus_id = request.POST.get('ticketstatus_id')
        status_date = datetime.strptime(request.POST['status_date'], '%d:%m:%Y %H:%M')
        description = 'Description of Ticket Admin Status'

        tickets = Ticket.objects.get(TID=ticket_id)
        tstatus = TicketStatus.objects.get(TSID=ticketstatus_id)
        tastatus = TickeAdminStatus (
            StatusDate = status_date,
            Ticket = tickets,
            TicketStatus = tstatus,
            Description = description,
        ) 
        tastatus.save()
        messages.success(request, 'Ticket Admin Status Has Been Saved Successfully!')
        return redirect('view_ticketAdminStatus')
    context = {
        'ticket':ticket,
        'ticketstatus':ticketstatus,
    }
    return render(request, 'Ticket/TicketAdminStatus/add_ticketAdminStatus.html', context)

def View_TicketAdminStatus(request):
    tastatus = TickeAdminStatus.objects.all()
    context = {
        'tastatus':tastatus,
    }
    return render(request, 'Ticket/TicketAdminStatus/view_ticketAdminStatus.html', context)

def Edit_TicketAdminStatus(request, id):
    ticket = Ticket.objects.all()
    ticketstatus = TicketStatus.objects.all()
    tastatus = TickeAdminStatus.objects.get(TASID=id)
    context = {
        'ticket':ticket,
        'ticketstatus':ticketstatus,
        'tastatus':tastatus,
    }
    return render(request, 'Ticket/TicketAdminStatus/edit_ticketAdminStatus.html', context)

def Update_TicketAdminStatus(request):
    if request.method == "POST":
        ticketas_id = request.POST.get('ticketas_id')
        ticket_id = request.POST.get('ticket_id')
        ticketstatus_id = request.POST.get('ticketstatus_id')
        status_date = datetime.strptime(request.POST['status_date'], '%d:%m:%Y %H:%M')

        ticket = Ticket.objects.get(TID=ticket_id)
        ticketstatus = TicketStatus.objects.get(TSID=ticketstatus_id)
        ticketas = TickeAdminStatus(
            TASID = ticketas_id,
            Ticket = ticket,
            TicketStatus = ticketstatus,
            StatusDate = status_date,
        )
        ticketas.save()
        messages.success(request, 'Ticket Admin Status has been updated successfully!')
        return redirect('view_ticketAdminStatus')
    return render(request, 'Ticket/TicketAdminStatus/view_ticketAdminStatus.html')

def Delete_TicketAdminStatus(request, id):
    tastatus = TickeAdminStatus.objects.get(TASID=id)
    tastatus.delete()
    messages.success(request, 'Ticket Status Has Been Deleted Successfully!')
    return redirect('view_ticketAdminStatus')

def Add_EFStatus(request):
    if request.method == "POST":
        fe_status = request.POST.get('fe_status')
        festatus = FEStatus(
            FEStatus = fe_status
        )
        festatus.save()
        messages.success(request, 'Field Engineer Status Has Been Saved Sucessfully!')
        return redirect('view_FEStatus')
    return render(request, 'Ticket/FEStatus/add_FEStatus.html')

def View_FEStatus(request):
    festatus = FEStatus.objects.all()
    context = {
        'festatus':festatus,
    }
    return render(request, 'Ticket/FEStatus/view_FEStatus.html', context)

def Edit_FEStatus(request, id):
    festatus = FEStatus.objects.get(FEID=id)
    context = {
        'festatus':festatus,
    }
    return render(request, 'Ticket/FEStatus/edit_FEStatus.html', context)

def Update_FEStatus(request):
    if request.method == "POST":
        festatus_id = request.POST.get('festatus_id')
        fe_status = request.POST.get('fe_status')
        festat = FEStatus.objects.get(FEID=festatus_id)
        festat.FEStatus = fe_status
        festat.save()
        messages.success(request, 'FE Status has been updated successfully')
        return redirect('view_FEStatus')
    return render(request, 'Ticket/FEStatus/view_FEStatus.html')

def Delete_FEStatus(request, id):
    festatus = FEStatus.objects.get(FEID=id)
    festatus.delete()
    messages.success(request, 'FE Status has been deleted successfully!')
    return redirect('view_FEStatus')

def Add_FEWork(request):
    festatus = FEStatus.objects.all()
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    if request.method == "POST":
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        festatus_id = request.POST.get('festatus_id')
        work_date = datetime.strptime(request.POST['work_date'], '%d:%m:%Y %H:%M')
        kilometer = request.POST.get('kilometer')

        tickets = Ticket.objects.get(TID=ticket_id)
        fenggg = FieldEngineer.objects.get(FEID=fengg_id)
        fstatus = FEStatus.objects.get(FEID=festatus_id)
        fwork = FEWork(
            Ticket = tickets,
            FEngg = fenggg,
            FStatus = fstatus,
            WorkDate = work_date,
            Kilometer = kilometer,
        )
        fwork.save()
        messages.success(request, 'Field Engineer Work Has Been Saved!')
        return redirect('view_FEWork')
    context = {
        'festatus':festatus,
        'ticket':ticket,
        'fengg':fengg,
    }
    return render(request, 'Ticket/FEWork/add_FEWork.html', context)

def View_FEWork(request):
    fework = FEWork.objects.all()
    context = {
        'fework':fework,
    }
    return render(request, 'Ticket/FEWork/view_FEWork.html', context)

def Edit_FEWork(request, id):
    fework = FEWork.objects.get(FEWID=id)
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    festatus = FEStatus.objects.all()
    context = {
        'fework':fework,
        'ticket':ticket,
        'fengg':fengg,
        'festatus':festatus,
    }
    return render(request, 'Ticket/FEWork/edit_FEWork.html', context)

def Update_FEWork(request):
    if request.method == "POST":
        few_id = request.POST.get('few_id')
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        festatus_id = request.POST.get('festatus_id')
        work_date = datetime.strptime(request.POST['work_date'], '%d:%m:%Y %H:%M')
        kilometer = request.POST.get('kilometer')

        tickets = Ticket.objects.get(TID=ticket_id)
        fenggg = FieldEngineer.objects.get(FEID=fengg_id)
        fstatus = FEStatus.objects.get(FEID=festatus_id)
        fwork = FEWork(
            FEWID = few_id,
            Ticket = tickets,
            FEngg = fenggg,
            FStatus = fstatus,
            WorkDate = work_date,
            Kilometer = kilometer,
        )
        fwork.save()
        messages.success(request, 'Field Engineer Work Has Been Saved!')
        return redirect('view_FEWork')
    return render(request, 'Ticket/FEWork/view_FEWork.html')

def Delete_FEWork(request, id):
    fwork = FEWork.objects.get(FEWID=id)
    fwork.delete()
    messages.success(request, 'Engineer Status Has Been Deleted Successfully!')
    return redirect('view_FEWork')

def Add_WorkActivity(request):
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    rclient = Client.objects.all()
    if request.method == "POST":
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        client_id = request.POST.get('client_id')
        activity_date = datetime.strptime(request.POST['activity_date'], '%d:%m:%Y %H:%M')
        work_details = request.POST.get('work_details')

        tickets = Ticket.objects.get(TID=ticket_id)
        feng = FieldEngineer.objects.get(FEID=fengg_id)
        client = Client.objects.get(ClientID=client_id)
        workactivity = WorkActivity(
            Ticket = tickets,
            FEngg = feng,
            RemoteClient = client,
            ActivityDate = activity_date,
            Description = work_details,
        )
        workactivity.save()
        messages.success(request, 'Activity work Has Been Saved!')
        return redirect('view_workActivity')
    context = {
        'ticket':ticket,
        'fengg':fengg,
        'rclient':rclient,
    }
    return render(request, 'Ticket/WorkActivity/add_workActivity.html', context)

def View_WorkActivity(request):
    workact = WorkActivity.objects.all()
    context = {
        'workact':workact,
    }
    return render(request, 'Ticket/WorkActivity/view_workActivity.html', context)

def Edit_WorkActivity(request, id):
    workactivity = WorkActivity.objects.get(WAID=id)
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    rclient = Client.objects.all()
    context = {
        'workactivity':workactivity,
        'ticket':ticket,
        'fengg':fengg,
        'rclient':rclient,
    }
    return render(request, 'Ticket/WorkActivity/edit_workActivity.html', context)

def Update_WorkActivity(request):
    if request.method == "POST":
        workactivity_id = request.POST.get('workactivity_id')
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        client_id = request.POST.get('client_id')
        activity_date = datetime.strptime(request.POST['activity_date'], '%d:%m:%Y %H:%M')
        work_details = request.POST.get('work_details')

        tickets = Ticket.objects.get(TID=ticket_id)
        feng = FieldEngineer.objects.get(FEID=fengg_id)
        client = Client.objects.get(ClientID=client_id)
        workactivity = WorkActivity(
            WAID = workactivity_id,
            Ticket = tickets,
            FEngg = feng,
            RemoteClient = client,
            ActivityDate = activity_date,
            Description = work_details,
        )
        workactivity.save()
        messages.success(request, 'Actiity work updated successfully!')
        return redirect('view_workActivity')
    return render(request, 'Ticket/WorkActivity/view_workActivity.html')

def Delete_WorkActivity(request, id):
    wactivty = WorkActivity.objects.get(WAID=id)
    wactivty.delete()
    messages.success(request, 'Work Activity has been deleted successfully!')
    return redirect('view_workActivity')

def Add_TicketExternalNotes(request):
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    if request.method == "POST":
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        exnote_date = datetime.strptime(request.POST['exnote_date'], '%d:%m:%Y %H:%M')
        notes = request.POST.get('notes')

        tickets = Ticket.objects.get(TID=ticket_id)
        fenginer = FieldEngineer.objects.get(FEID=fengg_id)
        texnotes = TicketExternalNotes(
            TicketNo = tickets,
            FieldEngineer = fenginer,
            Date = exnote_date,
            Notes = notes,
        )
        texnotes.save()
        messages.success(request, 'Ticket External Notes Has Been Saved')
        return redirect('view_ticketExternalNotes')
    context = {
        'ticket':ticket,
        'fengg':fengg,
    }
    return render(request, 'Ticket/TicketExternalNotes/add_ticketExternalNotes.html', context)

def View_TicketExternalNotes(request):
    ticketexnotes = TicketExternalNotes.objects.all()
    context = {
        'ticketexnotes':ticketexnotes,
    }
    return render(request, 'Ticket/TicketExternalNotes/view_ticketExternalNotes.html', context)

def Edit_TicketExternalNotes(request, id):
    ticketexnotes = TicketExternalNotes.objects.get(TENID=id)
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    context = {
        'ticketexnotes':ticketexnotes,
        'ticket':ticket,
        'fengg':fengg,
    }
    return render(request, 'Ticket/TicketExternalNotes/edit_ticketExternalNotes.html', context)

def Update_TicketExternalNotes(request):
    if request.method == "POST":
        ticketExternalNotes_id = request.POST.get('ticketExternalNotes_id')
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        exnote_date = datetime.strptime(request.POST['exnote_date'], '%d:%m:%Y %H:%M')
        notes = request.POST.get('notes')

        tickets = Ticket.objects.get(TID=ticket_id)
        fenginer = FieldEngineer.objects.get(FEID=fengg_id)
        texnotes = TicketExternalNotes(
            TENID = ticketExternalNotes_id,
            TicketNo = tickets,
            FieldEngineer = fenginer,
            Date = exnote_date,
            Notes = notes,
        )
        texnotes.save()
        messages.success(request, 'Ticket External Notes Has Been Updated Successfully!')
        return redirect('view_ticketExternalNotes')
    return render(request, 'Ticket/TicketExternalNotes/views_ticketExternalNotes.html')

def Delete_TicketExternalNotes(request, id):
    texnotes = TicketExternalNotes.objects.get(TENID=id)
    texnotes.delete()
    messages.success(request, 'Ticket External Note Has Been Deleted Successfully!')
    return redirect('view_ticketExternalNotes')

def Add_TicketInternalNotes(request):
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    if request.method == "POST":
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        innote_date = datetime.strptime(request.POST['innote_date'], '%d:%m:%Y %H:%M')
        notes = request.POST.get('notes')

        tickets = Ticket.objects.get(TID=ticket_id)
        fenginer = FieldEngineer.objects.get(FEID=fengg_id)
        texnotes = TicketInternalNotes(
            TicketNo = tickets,
            FieldEngineer = fenginer,
            Date = innote_date,
            Notes = notes,
        )
        texnotes.save()
        messages.success(request, 'Ticket Internal Notes Has Been Saved')
        return redirect('view_ticketInternalNotes')
    context = {
        'ticket':ticket,
        'fengg':fengg,
    }
    return render(request, 'Ticket/TicketInternalNotes/add_ticketInternalNotes.html', context)

def View_TicketInternalNotes(request):
    ticketinnotes = TicketInternalNotes.objects.all()
    context = {
        'ticketinnotes':ticketinnotes,
    }
    return render(request, 'Ticket/TicketInternalNotes/view_ticketInternalNotes.html', context)

def Edit_TicketInternalNotes(request, id):
    ticketinotes = TicketInternalNotes.objects.get(TINID=id)
    ticket = Ticket.objects.all()
    fengg = FieldEngineer.objects.all()
    context = {
        'ticketinotes':ticketinotes,
        'ticket':ticket,
        'fengg':fengg,
    }
    return render(request, 'Ticket/TicketInternalNotes/edit_ticketInternalNotes.html', context)

def Update_TicketInternalNotes(request):
    if request.method == "POST":
        ticketInternalNotes_id = request.POST.get('ticketInternalNotes_id')
        ticket_id = request.POST.get('ticket_id')
        fengg_id = request.POST.get('fengg_id')
        innote_date = datetime.strptime(request.POST['innote_date'], '%d:%m:%Y %H:%M')
        notes = request.POST.get('notes')

        tickets = Ticket.objects.get(TID=ticket_id)
        fenginer = FieldEngineer.objects.get(FEID=fengg_id)
        texnotes = TicketInternalNotes(
            TINID = ticketInternalNotes_id,
            TicketNo = tickets,
            FieldEngineer = fenginer,
            Date = innote_date,
            Notes = notes,
        )
        texnotes.save()
        messages.success(request, 'Ticket Internal Notes Has Been Updated Successfully!')
        return redirect('view_ticketInternalNotes')
    return render(request, 'Ticket/TicketInternalNotes/view_ticketInternalNotes.html')

def Delete_TicketInternalNotes(request, id):
    ticketinnotes = TicketInternalNotes.objects.get(TINID=id)
    ticketinnotes.delete()
    messages.success(request, 'Ticket Internal Note Has Been Deleted Successfully!!')
    return redirect('view_ticketInternalNotes')

def Add_TicketAgainstFE(request):
    ticket = Ticket.objects.all()
    fieldengg = FieldEngineer.objects.all()
    context = {
        'ticket':ticket,
        'fieldengg':fieldengg,
    }
    return render(request, 'Ticket/TicketAFE/add_ticketAgainstFE.html', context)

def Add_Billable(request):
    if request.method == "POST":
        billable = request.POST.get('billable')
        bable = BillAble(
            Billable = billable
        )
        bable.save()
        messages.success(request, 'Billable has been saved successfully!')
        return redirect('view_billable')
    return render(request, 'Billable/add_billable.html')

def View_Billable(request):
    billable = BillAble.objects.all()
    context = {
        'billable':billable,
    }
    return render(request, 'Billable/view_billable.html', context)

def Edit_Billable(request, id):
    billable = BillAble.objects.get(BAID=id)
    context = {
        'billable':billable,
    }
    return render(request, 'Billable/edit_billable.html', context)

def Update_Billable(request):
    if request.method == "POST":
        billable_id = request.POST.get('billable_id')
        billable = request.POST.get('billable')
        bable = BillAble.objects.get(BAID=billable_id)
        bable.Billable = billable
        bable.save()
        messages.success(request, 'Bill able has been updated successfully')
        return redirect('view_billable')
    return render(request, 'Billable/view_billable.html')

def Delete_Billable(request, id):
    billable = BillAble.objects.get(BAID=id)
    billable.delete()
    messages.success(request, 'Billable has been deleted successfully!')
    return redirect('view_billable')

def Add_TicketExpense(request):
    ticket = Ticket.objects.all()
    fengineer = FieldEngineer.objects.all()
    context = {
        'ticket':ticket,
        'fengineer':fengineer,
    }
    return render(request, 'Ticket/TicketExpense/add_ticketExpense.html', context)

# def Add_TicketExternalNotes(request):
#     return render(request, 'Ticket/add_ticketExternalNotes.html')

# def Add_TicketInternalNotes(request):
#     return render(request, 'Ticket/add_ticketInternalNotes.html')

def Add_TicketActionHistory(request):
    return render(request, 'Ticket/add_ticketActionHistory.html')

def Add_EnggWork(request):
    return render(request, 'Engineer/add_enggwork.html')

def View_EnggWork(request):
    return render(request, 'Engineer/view_enggwork.html')





def Add_Country(request):
    if request.method == "POST":
        CountryName = request.POST.get('CountryName')
        country = Country(
            CountryName = CountryName
        )
        country.save()
        messages.success(request, 'Country has been saved successfully')
        return redirect('view_country')
    return render(request, 'Country/add_country.html')

# def Add_Country(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = CountryForm()
#         else:
#             country = Country.objects.get(CountryID=id)
#             form = CountryForm(request.POST, instance=country)
#         return render(request, 'Country/add_country.html', {'form':form})
#     else:
#         if id == 0:
#             form = CountryForm(request.POST)
#         else:
#             country = Country.objects.get(CountryID=id)
#             form = CountryForm(request.POST, instance=country)
#         if form.is_valid():
#             form.save()
#         return redirect('view_country')



def View_Country(request):
    country = Country.objects.all()
    context = {
        'country':country
    }
    return render(request, 'Country/view_country.html', context)

def Edit_Country(request, id):
    country = Country.objects.get(CountryID=id)
    context = {
        'country':country
    }
    return render(request, 'Country/edit_country.html', context)

def Update_country(request):
    if request.method == "POST":
        CountryID = request.POST.get('CountryID')
        CountryName = request.POST.get('CountryName')
        country = Country.objects.get(CountryID=CountryID)
        country.CountryName = CountryName
        country.save()
        messages.success(request, 'Country has been updated successfully')
        return redirect('view_country')
    return render(request, 'Country/view_country.html')

def Delete_Country(request, id):
    country = Country.objects.get(CountryID=id)
    country.delete()
    messages.success(request, 'Country has been deleted successfully')
    return redirect('view_country')


def Add_Province(request):
    country = Country.objects.all()
    if request.method == "POST":
        country_id = request.POST.get('country_id')
        ProvinceName = request.POST.get('ProvinceName')
        country = Country.objects.get(CountryID=country_id)
        province = Province(
            ProvinceName = ProvinceName,
            Country = country,
        )
        province.save()
        messages.success(request, 'Province has been saved successfully')
        return redirect('view_province')
    context = {
        'country':country
    }
    return render(request, 'Province/add_province.html', context)

def View_Province(request):
    province = Province.objects.all()
    context = {
        'province':province
    }
    return render(request, 'Province/view_province.html', context)

def Edit_Province(request, id):
    province = Province.objects.get(ProvinceID=id)
    country = Country.objects.all()
    context = {
        'province': province,
        'country':country
    }
    return render(request, 'Province/edit_province.html', context)

def Update_Province(request):
    if request.method == "POST":
        country_id = request.POST.get('country_id')
        ProvinceID = request.POST.get('ProvinceID')
        ProvinceName = request.POST.get('ProvinceName')

        country = Country.objects.get(CountryID=country_id)
        province = Province.objects.get(ProvinceID=ProvinceID)

        province.ProvinceName = ProvinceName
        province.Country = country
        province.save()
        messages.success(request, 'Province has been updated successfully')
        return redirect('view_province')
    return render(request, 'Province/edit_province.html')

def Delete_Province(request, id):
    province = Province.objects.get(ProvinceID=id)
    province.delete()
    messages.success(request, 'Province has been deleted successfully')
    return redirect('view_province')


def Add_City(request):
    province = Province.objects.all()
    if request.method == "POST":
        ProvinceID = request.POST.get('ProvinceID')
        city_name = request.POST.get('city_name')
        province = Province.objects.get(ProvinceID=ProvinceID)
        city = City(
            CityName = city_name,
            Province = province,
        )
        city.save()
        messages.success(request, 'City has been saved Successfully!')
        return redirect('view_city')

    context = {
        'province':province
    }
    return render(request, 'City/add_city.html', context)

def View_City(request):
    city = City.objects.all()
    context = {
        'city':city,
    }
    return render(request, 'City/view_city.html', context)

def Edit_City(request, id):
    city = City.objects.get(CityID=id)
    province = Province.objects.all()
    context = {
        'city':city,
        'province':province,
    }
    return render(request, 'City/edit_city.html', context)

def Update_City(request):
    if request.method == "POST":
        ProvinceID = request.POST.get('ProvinceID')
        city_id = request.POST.get('city_id')
        city_name = request.POST.get('city_name')

        province = Province.objects.get(ProvinceID=ProvinceID)
        city = City.objects.get(CityID=city_id)

        city.CityName = city_name
        city.Province = province
        city.save()
        messages.success(request, 'City has been updated successfully')
        return redirect('view_city')
    return render(request, 'City/edit_city.html')

def Delete_City(request, id):
    city = City.objects.get(CityID=id)
    city.delete()
    messages.success(request, 'City has been deleted successfully')
    return redirect('view_city')

def Add_Area(request):
    city= City.objects.all()
    if request.method == "POST":
        city_id = request.POST.get('city_id')
        AreaName = request.POST.get('AreaName')
        city = City.objects.get(CityID=city_id)
        area = Area(
            AreaName = AreaName,
            City = city,
        )
        area.save()
        messages.success(request, "Area has been save successfully")
        return redirect('view_area')
    context = {
        'city':city
    }
    return render(request, 'Area/add_area.html', context)

def View_Area(request):
    area = Area.objects.all()
    context = {
        'area':area
    }
    return render(request, 'Area/view_area.html', context)

def Edit_Area(request, id):
    area = Area.objects.get(AreaID=id)
    city = City.objects.all()
    context = {
        'area':area, 'city':city
    }
    return render(request, 'Area/edit_area.html', context)

def Update_Area(request):
    if request.method == "POST":
        city_id = request.POST.get('city_id')
        AreaID = request.POST.get('AreaID')
        AreaName = request.POST.get('AreaName')

        city = City.objects.get(CityID=city_id)
        area = Area.objects.get(AreaID=AreaID)

        area.AreaName = AreaName
        area.City = city
        area.save()
        messages.success(request, 'Area has been updated successfully!')
        return redirect('view_area')
    return render(request, 'Area/edit_area.html')

def Delete_Area(request, id):
    area = Area.objects.get(AreaID=id)
    area.delete()
    messages.success(request, 'Area has been deleted successfully')
    return redirect('view_area')














def Add_EndClient(request):  
    return render(request, 'EndClient/add_endclient.html')

def Add_CustomerCategory(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        custcat = CustomerCategory(
            Name = Name
        )
        custcat.save()
        messages.success(request, 'Customer Category has been saved successfully')
        return redirect('view_customercategory')
    return render(request, 'CustomerCategory/add_customercategory.html')

def View_CustomerCategory(request):
    custcat = CustomerCategory.objects.all()
    context = {
        'custcat':custcat
    }
    return render(request, 'CustomerCategory/view_customercategory.html', context)

def Edit_CustomerCategory(request, id):
    custcat = CustomerCategory.objects.get(CustCatID=id)
    context = {
        'custcat':custcat
    }
    return render(request, 'CustomerCategory/edit_customercategory.html', context)

def Update_CustomerCategory(request):
    if request.method == "POST":
        CustCatID = request.POST.get('CustCatID')
        Name = request.POST.get('Name')
        custcat = CustomerCategory.objects.get(CustCatID=CustCatID)
        custcat.Name = Name
        custcat.save()
        messages.success(request, 'Customer Category has been updated successfully')
        return redirect('view_customercategory')
    return render(request, 'CustomerCategory/view_customercategory.html')

def Delete_CustomerCategory(request, id):
    custcat = CustomerCategory.objects.get(CustCatID=id)
    custcat.delete()
    messages.success(request, 'Country has been deleted successfully')
    return redirect('view_customercategory')

def Add_CustomerType(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        custtype = CustomerType(
            Name = Name
        )
        custtype.save()
        messages.success(request, "Customer Types has been saved successfully")
    return render(request, 'CustomerType/add_customertype.html')

def View_CustomerType(request):
    custtype = CustomerType.objects.all()
    context = {
        'custtype': custtype
    }
    return render(request, 'CustomerType/view_customertype.html', context)

def Edit_CustomerType(request, id):
    custtype = CustomerType.objects.get(CustTypeID=id)
    context = {
        'custtype': custtype
    }
    return render(request, 'CustomerType/edit_customertype.html', context)

def Update_CustomerType(request):
    if request.method == "POST":
        CustTypeID = request.POST.get('CustTypeID')
        Name = request.POST.get('Name')
        custtype =CustomerType.objects.get(CustTypeID=CustTypeID)
        custtype.Name = Name
        custtype.save()
        messages.success(request, 'Customer Type has baeen updated successfully')
        return redirect('view_customertype')
    return render(request, 'CustomerType/view_customertype.html')

def Delete_CustomerType(request, id):
    custtype = CustomerType.objects.get(CustTypeID=id)
    custtype.delete()
    messages.success(request, 'Customer Type has been deleted successfully')
    return redirect('view_customertype')

def Add_Customer(request):
    custcat = CustomerCategory.objects.all()
    cit = City.objects.all()
    custtype = CustomerType.objects.all()
    province = Province.objects.all()
    area = Area.objects.all()
    if request.method == "POST":
        CustCatID = request.POST.get('CustCatID')
        CityID = request.POST.get('CityID')
        CustTypeID = request.POST.get('CustTypeID')
        ProvinceID = request.POST.get('ProvinceID')
        AreaID = request.POST.get('AreaID')

        CustomerName = request.POST.get('CustomerName')
        ContactPerson = request.POST.get('ContactPerson')
        Designation = request.POST.get('Designation')
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        PhoneNo = request.POST.get('PhoneNo')
        WhatsAppNo = request.POST.get('WhatsAppNo')
        Address = request.POST.get('Address')
        Agents = request.POST.get('Agents')
        OpeningBalance = request.POST.get('OpeningBalance')
        CreditLimit = request.POST.get('CreditLimit')

        custcat = CustomerCategory.objects.get(CustCatID=CustCatID)
        cit = City.objects.get(CityID=CityID)
        custtype = CustomerType.objects.get(CustTypeID=CustTypeID)
        province = Province.objects.get(ProvinceID=ProvinceID)
        area = Area.objects.get(AreaID=AreaID)

        customer = Customers (
            CustomerName = CustomerName,
            ContactPerson = ContactPerson,
            Designation = Designation,
            Name = Name,
            Email = Email,
            PhoneNo = PhoneNo,
            WhatsAppNo = WhatsAppNo,
            Address = Address,
            Agents = Agents,
            OpeningBalance = OpeningBalance,
            CreditLimit = CreditLimit,
            CustomerCategory = custcat,
            City = cit,
            CustomerType = custtype,
            Province = province,
            Area = area
        )
        customer.save()
        messages.success(request, 'Customer Has Been Saved Successfully')
        return redirect('view_customer')
    context = {
        'custcat':custcat, 'cit':cit, 'custtype':custtype, 'province':province, 'area':area
    }
    return render(request, 'Customer/add_customer.html', context)

def View_Customer(request):
    cust = Customers.objects.all()
    context = {
        'cust': cust
    }
    return render(request, 'Customer/view_customer.html', context)

def Edit_Customer(request, id):
    cust = Customers.objects.get(CustomerID=id)
    custcat = CustomerCategory.objects.all()
    city = City.objects.all()
    custtype = CustomerType.objects.all()
    province = Province.objects.all()
    area = Area.objects.all()
    context = {
        'cust':cust, 'custcat':custcat, 'city':city, 'custtype':custtype, 'province':province, 'area':area
    }
    return render(request, 'Customer/edit_customer.html', context)

def Update_Customer(request):
    if request.method == "POST":

        CustomerID = request.POST.get('CustomerID')
        CustomerName = request.POST.get('CustomerName')
        ContactPerson = request.POST.get('ContactPerson')
        Designation = request.POST.get('Designation')
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        PhoneNo = request.POST.get('PhoneNo')


        CustCatID = request.POST.get('CustCatID')
        CityID = request.POST.get('CityID')
        CustTypeID = request.POST.get('CustTypeID')
        ProvinceID = request.POST.get('ProvinceID')
        AreaID = request.POST.get('AreaID')

        WhatsAppNo = request.POST.get('WhatsAppNo')
        Address = request.POST.get('Address')
        Agents = request.POST.get('Agents')
        CreditLimit = request.POST.get('CreditLimit')
        OpeningBalance = request.POST.get('OpeningBalance')
        

        custcat = CustomerCategory.objects.get(CustCatID=CustCatID)
        city = City.objects.get(CityID=CityID)
        custtype = CustomerType.objects.get(CustTypeID=CustTypeID)
        cust = Customers.objects.get(CustomerID=CustomerID)
        province = Province.objects.get(ProvinceID=ProvinceID)
        area = Area.objects.get(AreaID=AreaID)

        cust.CustomerName = CustomerName
        cust.ContactPerson = ContactPerson
        cust.Designation = Designation
        cust.Name = Name
        cust.Email = Email
        cust.PhoneNo = PhoneNo
        cust.WhatsAppNo = WhatsAppNo
        cust.Address = Address
        cust.Agents = Agents
        cust.CreditLimit = CreditLimit
        cust.OpeningBalance = OpeningBalance

        cust.CustomerCategory = custcat
        cust.Province = province
        cust.City = city
        cust.Area = area
        cust.CustomerType = custtype
        cust.save()

        messages.success(request, "Record Updated Successfully")
        return redirect('view_customer')
    return render(request, 'Customer/view_customer.html')

def Delete_Customer(request, id):
    cust = Customers.objects.get(CustomerID=id)
    cust.delete()
    messages.success(request, 'Customer has been deleted successfully')
    return redirect('view_customer')

def Add_Classes(request):
    if request.method == "POST":
        ClassName = request.POST.get('ClassName')
        cls = Classes(
            ClassName = ClassName
        )
        cls.save()
        messages.success(request, "Class has been saved successfully")
    return render(request, 'Inventory/Classes/add_classes.html')

def View_Classes(request):
    cls = Classes.objects.all()
    context = {
        'cls': cls
    }
    return render(request, 'Inventory/Classes/view_classes.html', context)

def Edit_Classes(request, id):
    cls = Classes.objects.get(ClassID=id)
    context = {
        'cls':cls
    }
    return render(request, 'Inventory/Classes/edit_classes.html', context)

def Update_Classes(request):
    if request.method == "POST":
        ClassID = request.POST.get('ClassID')
        ClassName = request.POST.get('ClassName')
        cls = Classes.objects.get(ClassID=ClassID)
        cls.ClassName = ClassName
        cls.save()
        messages.success(request, 'Class has been updated successfully')
        return redirect('view_classes')
    return render(request, 'Inventory/Classes/view_classes.html')

def Delete_Classes(request, id):
    cls = Classes.objects.get(ClassID=id)
    cls.delete()
    messages.success(request, 'Class has been deleted successfully')
    return redirect('view_classes')

def Add_ProductCategory(request):
    if request.method == "POST":
        ProductCategoryName = request.POST.get('ProductCategoryName')
        prcat = ProductCategory (
            ProductCategoryName = ProductCategoryName
        )
        prcat.save()
        messages.success(request, "Product category has been saved!")
        return redirect('view_productcategory')
    return render(request, 'Inventory/ProductCategory/add_productcategory.html')

def View_ProductCategory(request):
    prcat = ProductCategory.objects.all()
    context = {
        'prcat':prcat
    }
    return render(request, 'Inventory/ProductCategory/view_productcategory.html', context)
    

def Edit_ProductCategory(request, id):
    prcat = ProductCategory.objects.get(ProductCategoryID=id)
    context = {
        'prcat': prcat
    }
    return render(request, 'Inventory/ProductCategory/edit_productcategory.html', context)

def Update_ProductCategory(request):
    if request.method == "POST":
        ProductCategoryID = request.POST.get('ProductCategoryID')
        ProductCategoryName = request.POST.get('ProductCategoryName')
        pcat = ProductCategory.objects.get(ProductCategoryID=ProductCategoryID)
        pcat.ProductCategoryName = ProductCategoryName
        pcat.save()
        messages.success(request, 'Product Category Has Been Updated Successfully')
        return redirect('view_productcategory')
    return render(request, 'Inventory/ProductCategory/view_productcategory.html')

def Delete_ProductCategory(request, id):
    prcat = ProductCategory.objects.get(ProductCategoryID=id)
    prcat.delete()
    messages.success(request, 'Product Category Has been deleted successfully')
    return redirect('view_productcategory')

def Add_Options(request):
    if request.method == "POST":
        OptionName = request.POST.get('OptionName')
        op = Options (
            OptionName = OptionName
        )
        op.save()
        messages.success(request, 'Options has been added successfully')
        return redirect('view_options')
    return render(request, 'Inventory/Options/add_options.html')

def View_Options(request):
    op = Options.objects.all()
    context = {
        'op': op
    }
    return render(request, 'Inventory/Options/view_options.html', context)

def Eidt_Options(request, id):
    op = Options.objects.get(OptionID=id)
    context = {
        'op': op
    }
    return render(request, 'Inventory/Options/edit_options.html', context)

def Update_Options(request):
    if request.method == "POST":
        OptionID = request.POST.get('OptionID')
        OptionName = request.POST.get('OptionName')
        op = Options.objects.get(OptionID=OptionID)
        op.OptionName = OptionName
        op.save()
        messages.success(request, 'Inventory/Options/view_options.html')
        return redirect('view_options')
    return render(request, 'Inventory/Options/view_options.html')

def Delete_Options(request, id):
    op = Options.objects.get(OptionID=id)
    op.delete()
    messages.success(request, "Option has been deleted")
    return redirect('view_options')





# def Edit_City(request, id):
#     city = City.objects.get(CityID=id)
#     country = Country.objects.all()
#     context = {
#         'city':city,
#         'country':country,
#     }
#     return render(request, 'City/edit_city.html', context)

# def Update_City(request):
#     if request.method == "POST":
#         country_id = request.POST.get('country_id')
#         city_id = request.POST.get('city_id')
#         city_name = request.POST.get('city_name')

#         country = Country.objects.get(CountryID=country_id)
#         city = City.objects.get(CityID=city_id)

#         city.CityName = city_name
#         city.Country = country
#         city.save()
#         messages.success(request, 'City has been updated successfully')
#         return redirect('view_city')
#     return render(request, 'City/edit_city.html')

# def Delete_City(request, id):
#     city = City.objects.get(CityID=id)
#     city.delete()
#     messages.success(request, 'City has been deleted successfully')
#     return redirect('view_city')



# def Add_CustomerType(request):
#     if request.method == "POST":
#         Name = request.POST.get("Name")
#         custtype = CustomerType(
#             Name = Name
#         )
#         custtype.save()
#         messages.success(request, "Customer Types has been saved successfully")
#     return render(request, 'CustomerType/add_customertype.html')

# def View_Classes(request):
#     cls = Classes.objects.all()
#     context = {
#         'cls': cls
#     }
#     return render(request, 'Inventory/Classes/view_classes.html', context)

# def Edit_CustomerType(request, id):
#     custtype = CustomerType.objects.get(CustTypeID=id)
#     context = {
#         'custtype': custtype
#     }
#     return render(request, 'CustomerType/edit_customertype.html', context)

# def Update_CustomerType(request):
#     if request.method == "POST":
#         CustTypeID = request.POST.get('CustTypeID')
#         Name = request.POST.get('Name')
#         custtype =CustomerType.objects.get(CustTypeID=CustTypeID)
#         custtype.Name = Name
#         custtype.save()
#         messages.success(request, 'Customer Type has baeen updated successfully')
#         return redirect('view_customertype')
#     return render(request, 'CustomerType/view_customertype.html')

# def Delete_CustomerType(request, id):
#     custtype = CustomerType.objects.get(CustTypeID=id)
#     custtype.delete()
#     messages.success(request, 'Customer Type has been deleted successfully')
#     return redirect('view_customertype')

