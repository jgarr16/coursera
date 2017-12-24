# this program categorizes the mbox-short.txt email string by the day that the message was
# sent. it will count the number of messages by the day that they were sent.

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0 : print x
