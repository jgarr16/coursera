# Chapter 8, ex5 reads through mbox-short.txt and extracts the sender's email address
# then gives a count of all the lines that start with 'From' (not 'From:')

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'DEBUG:', words
    # if len(words) < 3: continue
    # if words[0] != 'From': continue
    if (len(words) >= 2) and (words[0] == 'From'): 
    	print words[1]
    	count = count + 1
    # print 'Total:',count
    # print words[2]

print 'There were',count,'lines in the file with From as the first word'