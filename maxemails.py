# Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

# Read the file
fname = input ("Enter the file name: ")
fn = open(fname)
words = list()
#handles = list()
# Search for the 'From ' query. Consider the second words
counts = dict()
for line in fn:
    if line.startswith('From '):
        words = line.split()
#        handles = handles + words[1]
#        print(handles)
        emails = words[1]
        counts[emails] = counts.get(emails,0) + 1
#        for word in words:
#            counts[word] = counts.get(word,0) + 1
#print(counts)
# Create a dictionary and use nested loop to count from the list above
#counts = dict()
#for word in counts:
#    counts.get(word, 0) + 1
#    print(counts)
# Use nested loop to find maxemails
bighandle = None
bigcount = None
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bighandle = k
        bigcount = v
print(bighandle, bigcount)
