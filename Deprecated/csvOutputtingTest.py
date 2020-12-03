import csv

value0 = '7:20'
value1 = '8:18'
value2 = '9:21'
value3 = '10:49'
value4 = '11:48'
value5 = '12:59'
value6 = '1:57'

clsTimes = value0, value1, value2, value3, value4, value5, value6

with open('clsTimes.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=' ')
    csv_writer.writerow(clsTimes)

print(csv)
