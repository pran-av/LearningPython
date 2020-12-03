# Ask for file input, default to mboxshort.txt
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fn = open(fname)
# Create a list and use split function (use :) to store 'hour' from the Form line
# Create a dictionary, choose the 1st index and count the number of hours
hours = list()
counts = dict()
for line in fn:
    if line.startswith('From '):
        hours = line.split()
#        print(hours)
        hours = hours[5].split(':')
#        hour = hours[0]
#        print(hour)
        counts[hours[0]] = counts.get(hours[0],0) + 1
#        print(hour[0], counts)
print("Final", counts)
# Print the count sorted by hours in ascending
for k, v in sorted(counts.items()):
    print(k,v)
