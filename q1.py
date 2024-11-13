import sqlite3
import datetime
conn = sqlite3.connect('schedule.db')
c = conn.cursor()
today = datetime.date.today()
formatted_date = today.strftime("%d.%m.%Y")
a = c.execute('''SELECT * FROM timetable WHERE day = ? ''', (formatted_date,)).fetchall()

for i in a:
	print(i)
conn.commit()
conn.close()