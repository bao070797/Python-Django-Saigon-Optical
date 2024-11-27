from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from sgperscription.models import PerscriptionInfo
from sgsaleorder.models import SaleorderInfo
from .forms import SignUpForm, AddRecordForm
from sgoptometrist.models import OptometristInfo
from .models import CustomerInfo
from django.db.models import Q
import mysql.connector
# from django.http import HttpResponse

mydb = mysql.connector.connect(
                        host="127.0.0.1",
                        user="root",
                        password="Bao@070797",
                        database="sg"
                        )
mycursor = mydb.cursor()
view_store = """select * from sg.sgcustomer_customerinfo"""


def home(request):
    # return HttpResponse('<h1>Saigon Customer</h1>')

    # Show data table with all the data we have.
    if request.GET.get('search'): # If there is a search in the url 
        search = request.GET['search']
        if search:
            q = Q()
            for field in CustomerInfo._meta.get_fields():
                query = "{}__icontains".format(field.name)
                q = q | Q(**{ query: request.GET['search'] })
            records = CustomerInfo.objects.filter(q)
        else:
            records = CustomerInfo.objects.all()    
    else:
        records = CustomerInfo.objects.all()
        #records = CustomerInfo.objects.raw("SELECT * FROM SG.SGCUSTOMER_CUSTOMERINFO WHERE CUST_DOB = '1997-07-07' ORDER BY CUST_NM_FIRST")


    # If you are not logged in yet
    if request.method == 'POST':
        usernamey = request.POST['username'] # Checks if there is username in the username input of customer.html
        passwordy = request.POST['password'] # Checks if there is password in the password input of customer.html
        # Authenticate
        user = authenticate(request, username = usernamey, password = passwordy)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('sgcustomer-home')
        else:
            messages.success(request, "There is an error logging in. Please try again")
            return redirect('sgcustomer-home')
    else:
        return render(request, 'customer.html', {'records':records})

#def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have sucessfully logged out")
    return redirect('sgcustomer-home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username'] # form.cleaned_data takes whatever username you've posted on the form and pulls it to assign to the username variable.
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password) 
            login(request, user)
            messages.success(request, "You have successfully registered.")
            return redirect('sgcustomer-home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form}) # Lets you enter the SignUpForm class from form.py in the form variable
    
    return render(request, 'register.html', {'form':form})


# Looking up the records
def customer_record(request, pk):
    if request.user.is_authenticated:
        customerrecord = CustomerInfo.objects.get(id=pk)
        prescriptions = PerscriptionInfo.objects.filter(cust_id=pk).order_by('-eff_dt')
        saleOrders = SaleorderInfo.objects.filter(customer_id=pk)
        return render(request, 'record.html', {'customer_record':customerrecord, 'prescriptions': prescriptions, 'saleOrders': saleOrders})
    else:
        messages.success(request, "You must be logged in to view the record...")
        return redirect('sgcustomer-home')


# Initialize Created_User and Updated_User as username
def populate_exclude_field(request, form):
        if form.instance.id is None:
            form.instance.created_user = form.instance.updated_user = request.user.username
        else:
            form.instance.updated_user = request.user.username
        return form

# Add customers    
def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        results = OptometristInfo.objects.all 
            
        if request.method == 'POST':
            if form.is_valid():
                values = []
                
                for field in form:
                    values.append(field.data)

                currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                currentUser = request.user.username
                values.append(currentDateTime)
                values.append(currentUser)
                values.append(currentDateTime)
                values.append(currentUser)
                values.append(currentDateTime)
                values.append(currentDateTime)
                values.append(currentDateTime)
                values.append("9999-12-31")
                print(values)
                sql = "INSERT INTO sgcustomer_customerinfo (cust_nm_first, cust_nm_last, cust_dob, cust_gender,"
                sql += "cust_addr, cust_suite_addr, cust_city, cust_prov, cust_cntry, "
                sql += "cust_pstl_cd, cust_email, cust_website, cust_tel_num_w, "
                sql += "cust_tel_num_m, cust_rt, cust_optmtrst_id, "
                sql += "cust_insurance_nm, cust_insurance_policy, cust_cr_dr_amt, note, "
                sql += "created_dt, created_user, updated_dt, updated_user, eff_dt, "
                sql += "cust_strt_dt, cust_end_dt, exp_dt) VALUES (%s,%s,%s,%s, "
                sql += "%s,%s,%s,%s,%s,"
                sql += "%s,%s,%s,%s, "
                sql += "%s,%s,%s, "
                sql += "%s,%s,%s,%s, "
                sql += "%s,%s,%s,%s,%s, "
                sql += "%s,%s,%s)"
                mycursor.execute(sql, values)
                mydb.commit()
                return redirect('sgcustomer-home')
            
            return render(request, 'add.html', {"form": form, "results":results})

        print(form)
        return render(request, 'add.html', {"form": form, "results":results})
    else:
        messages.success(request, "You must be logged in")
        return redirect('sgcustomer-home')
    

# Update customer records
def update_record(request, pk):
    if request.user.is_authenticated:
        current_product = CustomerInfo.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_product)
        results = OptometristInfo.objects.all
        if form.is_valid():
                values = []
                
                for field in form:
                    values.append(field.data)

                currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                currentUser = request.user.username
                values.append(currentDateTime)
                values.append(currentUser)
                values.append(currentDateTime)
                values.append(currentUser)
                values.append(currentDateTime)
                values.append(currentDateTime)
                values.append(currentDateTime)
                values.append("9999-12-31")
                values.append(pk)
                
                sql = "UPDATE sgcustomer_customerinfo set cust_nm_first = %s, cust_nm_last = %s, cust_dob = %s, cust_gender = %s," 
                sql += "cust_addr = %s, cust_suite_addr = %s, cust_city = %s, cust_prov = %s, cust_cntry = %s,"
                sql += "cust_pstl_cd = %s, cust_email = %s, cust_website = %s, cust_tel_num_w = %s,"
                sql += "cust_tel_num_m = %s, cust_rt = %s, cust_optmtrst_id = %s,"
                sql += "cust_insurance_nm = %s, cust_insurance_policy = %s, cust_cr_dr_amt = %s, note = %s,"
                sql += "created_dt = %s, created_user = %s, updated_dt = %s, updated_user = %s, eff_dt = %s,"
                sql+= "cust_strt_dt = %s, cust_end_dt = %s, exp_dt = %s where id = %s"
                mycursor.execute(sql, values)
                mydb.commit()
                return redirect('sgcustomer-home')
            
        return render(request, 'update.html', {"form": form, "results":results})
    else:
        messages.success(request, "You must be logged in")
        return redirect('sgcustomer-home')
    
# Redirect to perscription
def homeprescription (request):
    return render(request, 'perscription.html')

# Redirect to product
def homeproduct (request):
    return render(request, 'product.html')
