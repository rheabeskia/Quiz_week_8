import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

# Fetch the values from the database
# get the names of all tables in the database
query = """
    SELECT name FROM sqlite_master WHERE type='table';
    """

cursor.execute(query)
tables = cursor.fetchall()
# print(tables)

# tables = one table called ClimateData

# get the column names from ClimateData table
query = f"""
    SELECT * FROM ClimateData
    """
cursor.execute(query)
columns = sqlite3.Row(cursor, (1,)).keys()
# print(columns)

#for column in columns:
#    print(column)

data = cursor.fetchall()
#print(data)

# and populate some Python lists with the corresponding values
years = []
co2 = []
temp = []

for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# print(f"Years: {years}", f"CO2: {co2}", f"Temp: {temp}", sep="\n")

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
