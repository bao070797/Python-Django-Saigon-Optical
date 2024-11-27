from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import PerscriptionInfo
import os

# Create/Add Records

class AddPrescriptionRecordForm(forms.ModelForm):

    cust_id                 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Customer ID", "class":"form-control"}), label="")
    cust_optmtrst_id        = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Optometrist ID", "class":"form-control"}), label="")
    strt_dt                 = forms.DateField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Start Date", "class":"form-control", "type":"date"}), label="")
    end_dt                  = forms.DateField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"End Date", "class":"form-control", "type":"date"}), label="")
    od_sphere               = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OD Sphere", "class":"form-control"}), label="")
    od_cylinder             = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OD Cylinder", "class":"form-control"}), label="")
    od_axis                 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OD Axis", "class":"form-control"}), label="")
    od_prism                = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OD Prism", "class":"form-control"}), label="")
    od_add                  = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OD Add", "class":"form-control"}), label="")
    od_bif_typ              = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OD BIF Type", "class":"form-control"}), label="")
    od_seg_ht               = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OD SEG HT", "class":"form-control"}), label="")
    os_sphere               = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OS Sphere", "class":"form-control"}), label="")
    os_cylinder             = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OS Cylinder", "class":"form-control"}), label="")
    os_axis                 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OS Axis", "class":"form-control"}), label="")
    os_prism                = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OS Prism", "class":"form-control"}), label="")
    os_add                  = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OS Add", "class":"form-control"}), label="")
    os_bif_typ              = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OS BIF Type", "class":"form-control"}), label="")
    os_seg_ht               = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"OS SEG HT", "class":"form-control"}), label="")
    #note                    = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Notes", "class":"form-control"}), label="")


    class Meta:
        model = PerscriptionInfo
        exclude = ['created_user', 'updated_user', 'eff_dt', 'exp_dt']
        #exclude = ('created_dt', 'created_user', 'updated_dt', 'updated_user')
        #fields = ('cust_nm_first', 'cust_nm_last', 'cust_dob', 'cust_gender', 'cust_addr', 'cust_strt_nm','cust_city','cust_prov','cust_cntry','cust_pstl_cd','cust_email','cust_website','cust_tel_num_w','cust_tel_num_m','cust_rt','cust_optmtrst_id','cust_insurance_nm','cust_insurance_policy','cust_cr_dr_amt')
