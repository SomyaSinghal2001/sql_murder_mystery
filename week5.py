import sqlite3
conn=sqlite3.connect("D:\\Somya\\prepinsta internship\\sql-murder-mystery.db")
cursor = conn.cursor()
query = '''
    SELECT *
    FROM crime_scene_report
    WHERE Date = '20180115' AND City = 'SQL City' AND TYPE = 'murder';
    '''
cursor.execute(query)

crime_scene_report = cursor.fetchall()
print(crime_scene_report)
conn.close()
