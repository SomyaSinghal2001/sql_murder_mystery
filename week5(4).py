import sqlite3
conn=sqlite3.connect("D:\\Somya\\prepinsta internship\\sql-murder-mystery.db")
cursor = conn.cursor()
cursor2 = conn.cursor()

query = '''
    SELECT *
    FROM get_fit_now_member
    WHERE membership_status = "gold" AND id ="48Z7A";
    '''
   
query2 = '''
    SELECT *
    FROM get_fit_now_member
    WHERE membership_status = "gold" AND id ="48Z55";
    ''' 
cursor.execute(query)
cursor2.execute(query2)

witness_details = cursor.fetchall()
witness_details_2 = cursor2.fetchall()

for person in witness_details:
    print("id:", person[0])
    print("person_id:", person[1])
    print("name:", person[2])
    print("membership_status:", person[4])
    print("\n")

for person in witness_details_2:
    print("id:", person[0])
    print("person_id:", person[1])
    print("name:", person[2])
    print("membership_status:",person[4])
    print("\n")
conn.close()