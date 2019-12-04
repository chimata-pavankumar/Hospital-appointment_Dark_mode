import psycopg2
mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='vasthadb')
mycursor = mydb.cursor()
if 'appointment' == 'true' and 'id' == 1:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 1')
    mydb.commit()
    mycursor.close()
elif 'appointment' == 'true' and 'id' == 2:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 2')
    mydb.commit()
    mycursor.close()
elif 'appointment' == 'true' and 'id' == 3:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 3')
    mydb.commit()
    mycursor.close()
elif 'appointment' == 'true' and 'id' == 4:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 4')
    mydb.commit()
    mycursor.close()
elif 'appointment' == 'true' and 'id' == 5:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 5')
    mydb.commit()
    mycursor.close()
elif 'appointment' == 'true' and 'id' == 6:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 6')
    mydb.commit()
    mycursor.close()
elif 'appointment' == 'true' and 'id' == 7:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 7')
    mydb.commit()
    mycursor.close()
elif 'appointment' == 'true' and 'id' == 8:
    mycursor.execute('UPDATE vastha_treatmen SET appointment = true WHERE id = 8')
    mydb.commit()
    mycursor.close()
else:
    mydb.commit()