import sqlite3
conn=sqlite3.connect("D:\\Somya\\prepinsta internship\\sql-murder-mystery.db")
cursor = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()

query = '''
    SELECT id, plate_number, car_make
    FROM drivers_license
    WHERE plate_number = "H42W0X";
    '''
   
query2 = '''
    SELECT id, plate_number, car_make
    FROM drivers_license
    WHERE plate_number = "0H42W2";
    '''
    
query3 = '''
    SELECT id, plate_number, car_make
    FROM drivers_license
    WHERE plate_number = "4H42WR";
    '''
    
cursor.execute(query)
cursor2.execute(query2)
cursor3.execute(query3)

suspect_details = cursor.fetchall()
suspect_details_2= cursor2.fetchall()
suspect_details_3 = cursor3.fetchall()


for person in suspect_details:
    print("id:", person[0])
    print("plate_number:", person[1])
    print("car_make:", person[2])
    print("\n")
    
for person in suspect_details_2:
    print("id:", person[0])
    print("plate_number:", person[1])
    print("car_make:", person[2])
    print("\n")
    
for person in suspect_details_3:
    print("id:", person[0])
    print("plate_number:", person[1])
    print("car_make:", person[2])
    print("\n")

conn.close()