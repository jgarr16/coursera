import sqlite3
import csv


# fname = input('Enter file name: ')
# if (len(fname) < 1):
#     fname = 'export.csv'

fname = 'export.csv'
f = open(fname, 'r')
next(f, None)  # skip the header row
reader = csv.reader(f)

sql = sqlite3.connect('caprs-v1.db')
cur = sql.cursor()


cur.execute('DROP TABLE IF EXISTS caprs_tickets')
cur.execute('''CREATE TABLE IF NOT EXISTS caprs_tickets
            ("Incident ID" text PRIMARY KEY, Urgency text, "Open Time" date, City text, "Brief Description" text, Contact text, Description text, "Initial Impact" text, "Last Updated By" date, "Update Time" time, "Updated By" text, "Close Time" date, "Closed By" text, Solution text)''')
for row in reader:
    cur.execute(
        "INSERT INTO caprs_tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
# for row in cur.execute('SELECT * FROM caprs_tickets'):
    # print(row[0],row[2],row[3])
f.close()
sql.commit()
sql.close()
