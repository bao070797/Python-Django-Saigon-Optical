from django.db import models

# from sgcustomer.models import CustomerInfo

class PerscriptionInfo(models.Model):
    cust_id                 = models.IntegerField()
    cust_optmtrst_id        = models.IntegerField()
    strt_dt                 = models.DateTimeField(auto_now_add=True)
    end_dt                  = models.DateTimeField(auto_now=True)
    od_sphere               = models.CharField(max_length=10)
    od_cylinder             = models.CharField(max_length=10)
    od_axis                 = models.CharField(max_length=10)
    od_prism                = models.CharField(max_length=10)
    od_add                  = models.CharField(max_length=10)
    od_bif_typ              = models.CharField(max_length=10)
    od_seg_ht               = models.CharField(max_length=10)
    os_sphere               = models.CharField(max_length=10)
    os_cylinder             = models.CharField(max_length=10)
    os_axis                 = models.CharField(max_length=10)
    os_prism                = models.CharField(max_length=10)
    os_add                  = models.CharField(max_length=10)
    os_bif_typ              = models.CharField(max_length=10)
    os_seg_ht               = models.CharField(max_length=10)
    created_dt              = models.DateTimeField(auto_now_add=True)
    created_user            = models.CharField(max_length=25)
    updated_dt              = models.DateTimeField(auto_now=True)
    updated_user            = models.CharField(max_length=25)    
    eff_dt                  = models.DateTimeField(null=True) # After updating table change to auto_now_add_
    exp_dt                  = models.DateTimeField(default='9999-12-31')
