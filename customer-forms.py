from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomerInfo
import os

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", 
                             widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'})) 
    # Widget is to let us know the form field on the screen is a text-input-field/textbox.
    # attrs is to allow different attributes onto the page to style our forms.
    # The class is a bootstrap class
    first_name = forms.CharField(label="", 
                                 max_length=100, 
                                 widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", 
                                max_length=100, 
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        # Class meta is a class that contains the fields we require for the forms.py
        # The fields are from the auth_user of the database we're using in mysql
        # You need two sets of passwords in order to compare the two to make sure the user isn't typing a typo

    
    # This is to add the attributes to the username and password 1 and 2 similar to the email, first_name and last_name
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# Create/Add Records


class AddRecordForm(forms.ModelForm):

    cust_nm_first           = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    cust_nm_last            = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    cust_dob                = forms.DateField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Date of Birth (YYYY-MM-DD)", "class":"form-control", "type":"date"}), label="")
    cust_gender             = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Gender", "class":"form-control"}), label="")
    cust_addr               = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control", "id": "custAddress"}), label="")
    cust_suite_addr         = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Suite Address", "class":"form-control"}), label="")
    cust_city               = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    cust_prov               = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Province", "class":"form-control"}), label="")
    cust_cntry              = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Country", "class":"form-control"}), label="")
    cust_pstl_cd            = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code", "class":"form-control"}), label="")
    cust_email              = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    cust_website            = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Website", "class":"form-control"}), label="")
    cust_tel_num_w          = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number - Work", "class":"form-control"}), label="")
    cust_tel_num_m          = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number - Mobile", "class":"form-control"}), label="")
    cust_rt                 = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Customer Rate (1 -10)", "class":"form-control"}), label="")
    cust_optmtrst_id        = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Optometrist ID", "class":"form-control"}), label="")
    cust_insurance_nm       = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Insurance Name", "class":"form-control"}), label="")
    cust_insurance_policy   = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Insurance Policy", "class":"form-control"}), label="")
    cust_cr_dr_amt          = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Credit Rate Amount", "class":"form-control"}), label="")
    note                    = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Notes", "class":"form-control"}), label="")
    

    class Meta:
        model = CustomerInfo
        exclude = ['created_user', 'updated_user', 'eff_dt', 'exp_dt']
        #exclude = ('created_dt', 'created_user', 'updated_dt', 'updated_user')
        #fields = ('cust_nm_first', 'cust_nm_last', 'cust_dob', 'cust_gender', 'cust_addr', 'cust_strt_nm','cust_city','cust_prov','cust_cntry','cust_pstl_cd','cust_email','cust_website','cust_tel_num_w','cust_tel_num_m','cust_rt','cust_optmtrst_id','cust_insurance_nm','cust_insurance_policy','cust_cr_dr_amt')
