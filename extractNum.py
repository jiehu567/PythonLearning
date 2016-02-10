# Use the file name mbox-short.txt as the file name
# Extract number of each line beginning with X-DSPAM-Confidence:
# Calculate mean of these numbers
import re

fname = raw_input("Enter file name: ")
fh = open(fname)
num = 0.0
count = 0


    # firstly, I've tried the position method, but I prefer a general way for any float numbers
    # If only for this question, you can try: po = line.find("0.")
    # num = num + sum([float(s) for s in str.split() if s.isdigit()])

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    num_str = re.findall("\d+\.\d+", line)
    
    for i in num_str:
        num = num + float(i)
        count = count + 1

    

print num/count    
print "Done"

