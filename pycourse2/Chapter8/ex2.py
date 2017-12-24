# Chapter 8, ex2 and ex3 are included here. adjust comments for the pertinent portion
# ex2, the line that's still not 'guarded' was 'if len(words) == 0' - what if len was 2?

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'DEBUG:', words
    # if len(words) < 3: continue
    # if words[0] != 'From': continue
    if (len(words) >= 3) and (words[0] == 'From'): print words[2]
    # count = count + 1
    # print 'Total:',count
    # print words[2]