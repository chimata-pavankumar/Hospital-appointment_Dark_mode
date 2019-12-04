from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import treatmen
import psycopg2
# Create your views here.
def main(request):
    mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM vastha_treatmen WHERE id = 1')
    m = mycursor.fetchall()
    for i in m:
        id = i[0]
        doctor = i[2]
        treatments = i[3]
        appointment= i[5]
        if appointment is True:
            appointment = 'Not Available'
        else:
            appointment='Available'
        dates = i[1]
        price = i[4]
    mycursor.execute('select * from vastha_treatmen WHERE id=2')
    v = mycursor.fetchall()
    for i in v:
        doctor2 = i[2]
        treatments2 = i[3]
        appointment2 = i[5]
        if appointment2 is True:
            appointment2 = 'Not Available'
        else:
            appointment2 = 'Available'
        dates2 = i[1]
        price2 = i[4]
        id2= i[0]
    mycursor.execute('select * from vastha_treatmen WHERE id=3')
    v = mycursor.fetchall()
    for i in v:
        doctor3 = i[2]
        treatments3 = i[3]
        appointment3 = i[5]
        if appointment3 is True:
            appointment3 = 'Not Available'
        else:
            appointment3 = 'Available'
        dates3 = i[1]
        price3 = i[4]
        id3 = i[0]
    mycursor.execute('select * from vastha_treatmen WHERE id=4')
    v = mycursor.fetchall()
    for i in v:
        doctor4 = i[2]
        treatments4 = i[3]
        appointment4 = i[5]
        if appointment4 is True:
            appointment4 = 'Not Available'
        else:
            appointment4 = 'Available'
        dates4 = i[1]
        price4 = i[4]
        id4 = i[0]
    mycursor.execute('select * from vastha_treatmen WHERE id=5')
    v = mycursor.fetchall()
    for i in v:
        doctor5 = i[2]
        treatments5 = i[3]
        appointment5 = i[5]
        if appointment5 is True:
            appointment5 = 'Not Available'
        else:
            appointment5 = 'Available'
        dates5 = i[1]
        price5 = i[4]
        id5 = i[0]
    mycursor.execute('select * from vastha_treatmen WHERE id=6')
    v = mycursor.fetchall()
    for i in v:
        doctor6 = i[2]
        treatments6 = i[3]
        appointment6 = i[5]
        if appointment6 is True:
            appointment6 = 'Not Available'
        else:
            appointment6 = 'Available'
        dates6 = i[1]
        price6 = i[4]
        id6 = i[0]
    mycursor.execute('select * from vastha_treatmen WHERE id=7')
    v = mycursor.fetchall()
    for i in v:
        doctor7 = i[2]
        treatments7 = i[3]
        appointment7 = i[5]
        if appointment7 is True:
            appointment7 = 'Not Available'
        else:
            appointment7 = 'Available'
        dates7 = i[1]
        price7 = i[4]
        id7 = i[0]
    mycursor.execute('select * from vastha_treatmen WHERE id=8')
    v = mycursor.fetchall()
    for i in v:
        doctor8 = i[2]
        treatments8 = i[3]
        appointment8 = i[5]
        if appointment8 is True:
            appointment8 = 'Not Available'
        else:
            appointment8 = 'Available'
        dates8 = i[1]
        price8 = i[4]
        id8 = i[0]
    return render(request, 'main.html', {'id':id, 'doctor':doctor, 'treatments':treatments,'appointment':appointment,'dates':dates,'price':price,'id2':id2, 'doctor2':doctor2, 'treatments2':treatments2,'appointment2':appointment2,'dates2':dates2,'price2':price2,'id3':id3,'doctor3':doctor3, 'treatments3':treatments3,'appointment3':appointment3,'dates3':dates3,'price3':price3,'id4':id4,'doctor4':doctor4, 'treatments4':treatments4,'appointment4':appointment4,'dates4':dates4,'price4':price4,'id5':id5,'doctor5':doctor5, 'treatments5':treatments5,'appointment5':appointment5,'dates5':dates5,'price5':price5,'id6':id6,'doctor6':doctor6, 'treatments6':treatments6,'appointment6':appointment6,'dates6':dates6,'price6':price6,'id7':id7,'doctor7':doctor7, 'treatments7':treatments7,'appointment7':appointment7,'dates7':dates7,'price7':price7,'id8':id8,'doctor8':doctor8, 'treatments8':treatments8,'appointment8':appointment8,'dates8':dates8,'price8':price8})
    #return HttpResponse('NOT workED')