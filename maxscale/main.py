import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='',
    host='12.0.0.7',
    port=4003,
    database='zipcodes'
)

cursor = cnx.cursor()

query1 = "SELECT MAX(zipcode) FROM zipcodes_one"
cursor.execute(query1)
largest_zipcode = cursor.fetchone()[0]
print(largest_zipcode)

query2 = "SELECT zipcode FROM zipcodes_one WHERE state='KY'"
cursor.execute(query2)
ky_zipcodes = cursor.fetchall()
for zipcode in ky_zipcodes:
    print(zipcode[0])

query3 = "SELECT zipcode FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000"
cursor.execute(query3)
zipcodes_range = cursor.fetchall()
for zipcode in zipcodes_range:
    print(zipcode[0])

query4 = "SELECT TotalWages FROM zipcodes_one WHERE state='PA'"
cursor.execute(query4)
pa_wages = cursor.fetchall()
for wage in pa_wages:
    print(wage[0])

cursor.close()
cnx.close()
