import sqlite3
import csv


cols = ["Name", "Display Id", "Type", "Requested By", "Found By", "State", "Team Name", "Portfolio Item Display Id",
        "Created By Name", "Core?", "Closed Date", "Closed By Name", "Release Name"]
sql = sqlite3.connect('caprs-v1.db')
cur = sql.cursor()


cur.execute(
    'SELECT "Display Id","Requested By" FROM V1_tickets WHERE "Requested By" LIKE "%IM1_______%" ')
result = cur.fetchall()
match_list = []
count = 0
sql.commit()

print()
print('Begin CAPRS print run')
print()
for i in range(len(result)):
    cycle = i
    if len(result[cycle][1]) > 9:
        carve = result[cycle][1]
        if carve[0:3] == 'IM1':
            print("{0:3}".format(cycle + 1),
                  result[cycle][0][0:7], ' - ', result[cycle][1][0:10])
            match_list.append([result[cycle][0][0:7], result[cycle][1][0:10]])
            count = cycle + 1


cur.execute(
    'SELECT "Display Id","Found By" FROM V1_tickets WHERE "Found By" LIKE "%IM1_______%" ')
result2 = cur.fetchall()
sql.commit()

for i in range(len(result2)):
    cycle = i
    if len(result2[cycle][1]) > 9:
        carve = result2[cycle][1]
        if carve[0:3] == 'IM1':
            print("{0:3}".format(count + cycle + 1),
                  result2[cycle][0][0:7], ' - ', result2[cycle][1][0:10])
            match_list.append([result2[cycle][0][0:7], result2[cycle][1][0:10]])


print()
print('Processed', len(result) + len(result2), 'Records')
print('         ', len(result), 'Stories\n         ', len(result2), 'Defects')
print('End of CAPRS print run')
print()

# print(match_list)

# write match_list to CSV
CAPRS_V1_csv = 'CAPRS_V1.csv'
with open('CAPRS_V1.csv', 'w') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["V1 Story/Defect", "CAPRS IM"])
    for val in match_list:
        writer.writerows([val])

sql.commit()
sql.close()


# 'IM1\d+'
# SQL Search statement: SELECT "Display Id","Requested By" FROM V1_tickets WHERE ("Requested By" LIKE "IM1_______" or "Requested By" LIKE "IM1_______ & IM1_______"  or "Requested By" LIKE "IM1_______, IM1_______" or  "Requested By" LIKE "IM1_______ and IM1_______")
