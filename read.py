import pandas as pd
import sqlite3
file =pd.read_csv("schedule.txt", sep=";", encoding='utf-8')
for index,row in file.iterrows():
    print(index, row[2])
    
conn = sqlite3.connect('schedule.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXIStS timetable
          (day TEXT, time TEXT, course TEXT, class TEXT, typel TEXT, teacher TEXT)''')

for index,row in file.iterrows():
    c.execute('''INSERT INTO timetable (day, time, course, class, typel, teacher) VALUES (?, ?, ?, ?, ?, ?)''',(row[0], row[1], row[2], row[3], row[4], row[5])) 
print ("база данных заполнена")
conn.commit()
conn.close()