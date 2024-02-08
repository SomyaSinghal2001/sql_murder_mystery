import sqlite3

# Connect to the database
conn = sqlite3.connect('D:\\Somya\\prepinsta internship\\sql-murder-mystery.db')
cursor = conn.cursor()
cursor2 = conn.cursor()

# Define the query to retrieve witness details
query = '''
    SELECT name,address_number,address_street_name,id,ssn
    FROM person
    WHERE address_street_name = "Northwestern Dr" AND address_number = "4919";
'''
query2 = '''
    SELECT name,address_number,address_street_name,id,ssn
    FROM person
    WHERE address_street_name = "Franklin Ave" AND name = "Annabel Miller";
    '''
# Execute the query
cursor.execute(query)
cursor2.execute(query2)

# Fetch all the results
witness_details = cursor.fetchall()
witness_details_2 = cursor2.fetchall()

# Display or process the results as needed
for person in witness_details:
    print("Name:", person[0])
    print("address_number:", person[1])
    print("address_street_name:", person[2])
    print("id:", person[3])
    print("ssn:", person[4])
    print("\n")

for person in witness_details_2:
    print("Name:", person[0])
    print("address_number:", person[1])
    print("address_street_name:", person[2])
    print("id:", person[3])
    print("ssn:", person[4])
    print("\n")
# Close the connection
conn.close()
