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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
telnums = set()

for text in texts:
    telnums.add(text[0])
    telnums.add(text[1])

for call in calls:
    telnums.add(call[0])
    telnums.add(call[1])

print(f'There are {len(telnums)} different telephone numbers in the records.')
