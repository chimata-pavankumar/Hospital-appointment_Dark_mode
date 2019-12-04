from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
import psycopg2
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email = email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'passwords not matched')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def appointment(request):
    if request.method == "POST":
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        for p in m:
            doctor = p[2]
            date = str(p[1])
            data = 'you got appointment by {} at {}'.format(doctor,date)
            return render(request, 'appointment.html', {'data':data})
            #return render(request, 'appointment.html', {'doctor':doctor, 'date':date})
    return render(request,'appointment.html',{'result':'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_one(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 1')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_two(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 2')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_three(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 3')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_four(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 4')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_five(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 5')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_six(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 6')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_seven(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 7')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def dr_eight(request):
    if request.method=='POST':
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true where id = 8')
        mydb.commit();
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor, date)
            return render(request, 'appointment.html', {'data': data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def del_one(request):
    mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
    mycursor = mydb.cursor()
    mycursor.execute('UPDATE vastha_treatmen SET appointment = false where appointment = true')
    mydb.commit()
    return render(request, 'appointment.html',{'result':'you dont have any appointments'})

def aappointment(request):
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM vastha_treatmen WHERE appointment = true')
        m = mycursor.fetchall()
        if m:
            for p in m:
                doctor = p[2]
                date = str(p[1])
                data = 'you got appointment by {} at {}'.format(doctor,date)
            return render(request, 'appointment.html', {'data':data})
        return render(request, 'appointment.html', {'result': 'NO APPOINTMENT HAS TAKEN TILL NOW'})

def logout(request):
    auth.logout(request)
    return redirect('/')

def python(request):
    mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
    mycursor = mydb.cursor()
    if id == 1:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 1')
        mydb.commit()
        mycursor.close()
    elif 'id' == 2:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 2')
        mydb.commit()
        mycursor.close()
    elif 'id' == 3:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 3')
        mydb.commit()
        mycursor.close()
    elif 'id' == 4:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 4')
        mydb.commit()
        mycursor.close()
    elif 'id' == 5:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 5')
        mydb.commit()
        mycursor.close()
    elif 'id' == 6:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 6')
        mydb.commit()
        mycursor.close()
    elif  'id' == 7:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 7')
        mydb.commit()
        mycursor.close()
    elif 'id' == 8:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 8')
        mydb.commit()
        mycursor.close()
    else:
        mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 8')
        mydb.commit()
        mycursor.close()
    return render(request,'index.html')