from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomerInfo(models.Model):
    cust_nm_first           = models.CharField(max_length=50)
    cust_nm_last            = models.CharField(max_length=50)
    cust_dob                = models.DateField()
    cust_gender             = models.CharField(max_length=1)
    cust_addr               = models.CharField(max_length=50)
    cust_suite_addr         = models.CharField(max_length=50)
    cust_city               = models.CharField(max_length=50)
    cust_prov               = models.CharField(max_length=50)
    cust_cntry              = models.CharField(max_length=50)
    cust_pstl_cd            = models.CharField(max_length=20)
    cust_email              = models.CharField(max_length=100)
    cust_website            = models.CharField(max_length=200)
    cust_tel_num_w          = models.CharField(max_length=15)
    cust_tel_num_m          = models.CharField(max_length=15)
    cust_strt_dt            = models.DateTimeField(auto_now_add=True)
    cust_end_dt             = models.DateTimeField(auto_now=True)
    cust_rt                 = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    cust_optmtrst_id        = models.IntegerField()
    cust_insurance_nm       = models.CharField(max_length=75)
    cust_insurance_policy   = models.CharField(max_length=75)
    cust_cr_dr_amt          = models.DecimalField(max_digits = 8, decimal_places = 2)
    note                    = models.CharField(max_length=250, default=None, blank=True)
    created_dt              = models.DateTimeField(auto_now_add=True)
    created_user            = models.CharField(max_length=25)
    updated_dt              = models.DateTimeField(auto_now=True)
    updated_user            = models.CharField(max_length=25)
    eff_dt                  = models.DateTimeField(null=True) # After updating table change to auto_now_add_
    exp_dt                  = models.DateTimeField(default='9999-12-31')

    def __str__(self):
        return(f"{self.cust_nm_first} {self.cust_nm_last}")

