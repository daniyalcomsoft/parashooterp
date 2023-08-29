from dataclasses import field
from django import forms
from .models import *

# class EndClientForm(forms.ModelForm):

#     class Meta:
#         model = EndClient
#         fields = ('CompanyName','Address1','Address2','country','city')
#         labels = {
#             'CompanyName':'Company Name',
#             'country':'Country',
#             'city':'City'
#         }
#     def __init(self, *args, **kwargs):
#         super(EndClientForm,self).__init__(*args, **kwargs)
#         self.fields['country'].empty_label = 'Select Country'
#         self.fields['city'].empty_label = 'Select City'

# class CountryForm(forms.ModelForm):

#     class Meta:
#         model = Country
#         fields = ("CountryName",)
#         labels = {
#             'CountryName':'Country Name'
#         }
#     def __init__(self, *args, **kwargs):
#         super(CountryForm,self).__init__(*args, **kwargs)

