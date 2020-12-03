# Open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split() method. The program
# should build a list of words. For each word on each line check to see if the
# word is already in the list and if not append it to the list.When the program
# completes, sort and print the resulting words in alphabetical order.
# You can download the sample Daten at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fn = open(fname)
lst2 = list()
lst = list()
for line in fn:
    lst = lst + line.split()
#    lst.append(lst)
#    print(lst)
for i in range(len(lst)):
#    print(i)
    if lst[i] in lst2:
#        print(i, "already present!")
        continue
    lst2.append(lst[i])
#    print(lst[i], "added")
#for line in lst2:
print(sorted(lst2))
