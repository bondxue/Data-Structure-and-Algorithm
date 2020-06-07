"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
record_dict = {}

for call in calls:
    if call[0] not in record_dict:
        record_dict[call[0]] = 0
    if call[1] not in record_dict:
        record_dict[call[1]] = 0

    record_dict[call[0]] += int(call[3])
    record_dict[call[1]] += int(call[3])

max_record = max(record_dict, key=lambda k: record_dict[k])
print(f'{max_record} spent the longest time, {record_dict[max_record]} seconds, on the phone during September 2016.')