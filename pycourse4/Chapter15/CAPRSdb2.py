import sqlite3
import csv
import sys

db = sys.argv[1]
conn = sqlite3.connect(db)
conn.text_factory = str  # allows utf-8 data to be stored
c = conn.cursor()


fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'export.csv'
# f = open(fname, 'r')
# next(f, None) # skip the header row

while True:

    with open(fname, "r") as f:
        reader = csv.reader(f)
 
        header = True
        for row in reader:
            if header:
                # gather column names from the first row of the csv
                header = False
                tablename = "caprs_tickets"
 
                sql = '''DROP TABLE IF EXISTS %s''' % tablename
                c.execute(sql)
                sql = '''CREATE TABLE %s (%s)''' % (tablename, ", ".join([ "%s text" % column for column in row ]))
                c.execute(sql)
 
                for column in row:
                    if column.lower().endswith("_id"):
                        index = "%s__%s" % ( tablename, column )
                        sql = "CREATE INDEX %s on %s (%s)" % ( index, tablename, column )
                        c.execute(sql)
 
                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename,
                            ", ".join([ "?" for column in row ]))
 
                rowlen = len(row)
            else:
                # skip lines that don't have the right number of columns
                if len(row) == rowlen:
                    c.execute(insertsql, row)
 
        conn.commit()
 
# c.close()
conn.close()


# reader = csv.reader(f)

# sql = sqlite3.connect('caprs.db')
# cur = sql.cursor()


# cur.execute('DROP TABLE IF EXISTS caprs_tickets')
# cur.execute('''CREATE TABLE IF NOT EXISTS caprs_tickets
#             (IM text, Priority text, Opened date, City text, "Brief Description" text, "Opened By" text)''') 
# for row in reader:
#     cur.execute("INSERT INTO caprs_tickets VALUES (?, ?, ?, ?, ?, ?)", row)
# # for row in cur.execute('SELECT * FROM caprs_tickets'):
#     # print(row[0],row[2],row[3])
# f.close()
# sql.commit()
# sql.close()
