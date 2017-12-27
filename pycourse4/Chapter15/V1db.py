import sqlite3
import csv


# fname = input('Enter file name: ')
# if (len(fname) < 1):
#     fname = 'V1export.csv'

fname = 'V1export.csv'
f = open(fname, 'r')
next(f, None)  # skip the header row
reader = csv.reader(f)

sql = sqlite3.connect('caprs-v1.db')
cur = sql.cursor()


cur.execute('DROP TABLE IF EXISTS V1_tickets')
cur.execute('''CREATE TABLE IF NOT EXISTS V1_tickets
            ("Name" text, "Display Id" text PRIMARY KEY,"Type" text,"Requested By" text, "Found By" text, "State" text,"Team Name" text,"Portfolio Item Display Id" text,"Created By Name" text,"Core?" text,"Closed Date" date,"Closed By Name" text,"Release Name" text)''')
for row in reader:
    cur.execute(
        "INSERT INTO V1_tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
# for row in cur.execute('SELECT * FROM caprs_tickets'):
    # print(row[0],row[2],row[3])
f.close()
sql.commit()
sql.close()
