import sqlite3
conn=sqlite3.connect("D:\\Somya\\prepinsta internship\\sql-murder-mystery.db")
cursor = conn.cursor()
cursor2 = conn.cursor()

query = '''
    SELECT *
    FROM interview
    WHERE person_id = "14887";
    '''
    
query2 = '''
    SELECT *
    FROM interview
    WHERE person_id = "16371";
    '''
cursor.execute(query)
cursor2.execute(query2)

witness_details = cursor.fetchall()
witness_details_2 = cursor2.fetchall()

for person in witness_details:
    print("person_id:", person[0])
    print("transcript:", person[1])
    print("\n")

for person in witness_details_2:
    print("person_id:", person[0])
    print("transcript:", person[1])
    print("\n")
conn.close()