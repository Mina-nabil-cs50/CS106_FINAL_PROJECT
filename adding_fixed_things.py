'''import sqlite3

conn = sqlite3.connect("c:/Users/minas/OneDrive/Desktop/TERM 2/CS106-Project/database/hotel.db")
cursor = conn.cursor()
# Update these values as needed
cursor.execute("UPDATE staff SET username='admin', password='admin123' WHERE staff_role='admin';")
cursor.execute("UPDATE staff SET username='staff1', password='staff123' WHERE staff_role='staff';")
conn.commit()
conn.close()
print("Sample users added.")'''