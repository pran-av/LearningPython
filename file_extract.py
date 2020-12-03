# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as shown
# below. Do not use the sum() function or a variable named sum in your solution.

fname = input('Enter the file name: ')
file = open(fname)
count = 0
tot = 0
for sentence in file:
    if not sentence.startswith('X-DSPAM-Confidence:'):
         continue
    pos = sentence.find(':')
    tot = float(tot) + float(sentence[pos+1:].strip())
#    print(sentence[pos+1:].strip())
    count = count + 1
#print(count)
avg = tot/count
print('Average spam confindence:', avg)
