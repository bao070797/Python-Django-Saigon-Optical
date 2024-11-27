from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .forms import AddPrescriptionRecordForm
from .models import PerscriptionInfo
from django.db.models import Q
import mysql.connector

mydb = mysql.connector.connect(
                        host="127.0.0.1",
                        user="root",
                        password="Bao@070797",
                        database="sg"
                        )
mycursor = mydb.cursor()
view_prescription = """select * from sg.sgperscription_perscriptioninfo"""
#view_perscription = PerscriptionInfo.objects.raw("select * from sg.sgperscription_perscriptioninfo")


# Create your views here without model.

def homeprescription (request):
    #perscription_data = PerscriptionInfo.objects.all()
    mycursor.execute(view_prescription)
    perscription_data = mycursor.fetchall()
    return render(request, 'perscription.html', {'records':perscription_data})

# Create your views here with model.

#def homeprescription (request):
#    records = []
#    if request.GET.get('search'): # If there is a search in the url 
#        search = request.GET['search']
#        if search:
#            q = Q()
#            for field in PerscriptionInfo._meta.get_fields():
#                query = "{}__icontains".format(field.name)
#                q = q | Q(**{ query: request.GET['search'] })
#            records = PerscriptionInfo.objects.filter(q)
#        else:
#            records = PerscriptionInfo.objects.raw("select * from sg.sgperscription_perscriptioninfo")
#    else:
#            records = CustomerInfo.objects.all()

#    records = PerscriptionInfo.objects.raw("select * from sg.sgperscription_perscriptioninfo")
#    
#    return render(request, 'perscription.html', {'records':records})


# View Prescription Record
def prescription_record(request, pk):
    if request.user.is_authenticated:
        mycursor.execute("select * from sg.sgperscription_perscriptioninfo where id = {}".format(pk))
        #perscriptionrecord = PerscriptionInfo.objects.get(id=pk)
        perscriptionrecord = mycursor.fetchone()
        return render(request, 'perscription_record.html', {'perscription_record':perscriptionrecord})
    else:
        messages.success(request, "You must be logged in to view the record...")
        return redirect('sgperscription-home')


# Add Prescription Record
def add_prescription(request):
    if request.user.is_authenticated:
        cust_id = request.GET.get('customerId', None)
        form = AddPrescriptionRecordForm(request.POST or None, initial={'cust_id': cust_id}) 
        # 65 and line 66 after None is new. Remember for adding products.
            
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
                values.append("9999-12-31")

                sql = "INSERT INTO sgperscription_perscriptioninfo (cust_id, cust_optmtrst_id, od_sphere, od_cylinder, od_axis, od_prism, od_add, od_bif_typ, od_seg_ht, os_sphere, os_cylinder, os_axis, os_prism, os_add, os_bif_typ, os_seg_ht, strt_dt, end_dt, created_dt, created_user, updated_dt, updated_user, eff_dt, exp_dt)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql, values)
                mydb.commit()
                return redirect('sgperscription-home')
            
            return render(request, 'add_perscription.html', {"form": form})

        print(form)
        return render(request, 'add_perscription.html', {"form": form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('sgperscription-home')



# Update Prescription
def update_prescription(request, pk):
    if request.user.is_authenticated:
        current_prescription = PerscriptionInfo.objects.get(id=pk)
        form = AddPrescriptionRecordForm(request.POST or None, instance=current_prescription)
        if form.is_valid():
                values = []
                
                for field in form:
                    values.append(field.data)

                currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                currentUser = request.user.username
                #values.append(currentDateTime)
                values.append(currentUser)
                values.append(currentDateTime)
                values.append(currentUser)
                #values.append(currentDateTime)
                values.append("9999-12-31")
                values.append(pk)

                sql = "UPDATE sgperscription_perscriptioninfo set cust_id = %s, cust_optmtrst_id = %s, od_sphere = %s, od_cylinder = %s, od_axis = %s, od_prism = %s, od_add = %s, od_bif_typ = %s, od_seg_ht = %s, os_sphere = %s, os_cylinder = %s, os_axis = %s, os_prism = %s, os_add = %s, os_bif_typ = %s, os_seg_ht = %s, strt_dt = %s, end_dt = %s, created_user = %s, updated_dt = %s, updated_user = %s, exp_dt = %s where id = %s"
                mycursor.execute(sql, values)
                mydb.commit()
                return redirect('sgperscription-home')
            
        return render(request, 'update_perscription.html', {"form": form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('sgperscription-home')
        
