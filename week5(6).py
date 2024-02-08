import sqlite3
conn=sqlite3.connect("D:\\Somya\\prepinsta internship\\sql-murder-mystery.db")
cursor = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()
cursor4 = conn.cursor()
cursor5 = conn.cursor()

query = '''
    SELECT *
    FROM person
    WHERE id = "183779";
    '''
   
query2 = '''
    SELECT *
    FROM person
    WHERE id = "423327";
    '''
    
query3 = '''
    SELECT *
    FROM person
    WHERE id = "664760";
    '''

query4 = '''
    SELECT *
    FROM person
    WHERE id = "28819";
    '''
    
query5 = '''
    SELECT *
    FROM person
    WHERE id = "67318";
    '''
       
cursor.execute(query)
cursor2.execute(query2)
cursor3.execute(query3)
cursor4.execute(query4)
cursor5.execute(query5)

suspect_details = cursor.fetchall()
suspect_details_2= cursor2.fetchall()
suspect_details_3 = cursor3.fetchall()
suspect_details_4 = cursor4.fetchall()
suspect_details_5 = cursor5.fetchall()

for person in suspect_details:
    print("id:", person[0])
    print("name:", person[1])
    print("address_number:", person[2])
    print("address_street_name:",person[3])
    print("\n")
    
for person in suspect_details_2:
    print("id:", person[0])
    print("name:", person[1])
    print("address_number:", person[2])
    print("address_street_name:",person[3])
    print("\n")
    
for person in suspect_details_3:
    print("id:", person[0])
    print("name:", person[1])
    print("address_number:", person[2])
    print("address_street_name:",person[3])
    print("\n")
    
for person in suspect_details_4:
    print("id:", person[0])
    print("name:", person[1])
    print("address_number:", person[2])
    print("address_street_name:",person[3])
    print("\n")
    
for person in suspect_details_5:
    print("id:", person[0])
    print("name:", person[1])
    print("address_number:", person[2])
    print("address_street_name:",person[3])
    print("\n")

conn.close()