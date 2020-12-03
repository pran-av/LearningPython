lst = ['apple', 'cake', 'cake', 'banana', 'apple']
lst2 = list()
for i in range(len(lst)):
#    if i == len(lst) - 1 :
#        print("continue trigerred")
#        continue
    if lst[i] in lst2:
        print(i, "already present")
        continue
    lst2.append(lst[i])
    print(lst[i], "added")
print(sorted(lst2))
print("END")
