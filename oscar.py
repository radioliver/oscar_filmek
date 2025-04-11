import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "oscar"
)

mycursor = mydb.cursor()

# mycursor.execute ("SELECT * FROM film")
# for x in mycursor:
#     print(f"{x}")


mycursor.execute ("SELECT ev, cim FROM film ORDER BY ev ASC LIMIT 20")
for x in mycursor:
    print(x)

mycursor.execute ("SELECT ev FROM film WHERE ev.count > 10")
for x in mycursor:
    print(x)