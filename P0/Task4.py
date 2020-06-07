"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

call_out = set([call[0] for call in calls])
call_in = set([call[1] for call in calls])
text_out = set([text[0] for text in texts])
text_in = set([text[1] for text in texts])

print( "These numbers could be telemarketers: " )
telemarketers = sorted(list(call_out-call_in-text_out-text_in))
for num in telemarketers:
    print(num)
