import sqlite3
import csv


# fname = input('Enter file name: ')
# if (len(fname) < 1):
#     fname = 'V1export.csv'

fname = 'V1_CAPRS_20171219.csv'
f = open(fname, 'r')
next(f, None)  # skip the header row
reader = csv.reader(f)

sql = sqlite3.connect('caprs-v1.db')
cur = sql.cursor()


cur.execute('DROP TABLE IF EXISTS V1_CAPRS_compare')
cur.execute('''CREATE TABLE IF NOT EXISTS V1_CAPRS_compare
            ("CAPRS" text, "Story/Defect" text,"Release" text,"Iteration" text,"Backlog Group" text)''')
for row in reader:
    cur.execute(
        "INSERT INTO V1_CAPRS_compare VALUES (?, ?, ?, ?, ?)", row)
# for row in cur.execute('SELECT * FROM caprs_tickets'):
    # print(row[0],row[2],row[3])
f.close()
sql.commit()
sql.close()
