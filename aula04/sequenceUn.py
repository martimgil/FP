"""
This program generates 20 terms of a sequence by a recurrence relation.
Change it to show all positive terms of the sequence and count them.
Format the columns to make the output look like this:
   n        Un
   0   100.000
   1    99.990
   2    99.980
"""

print("{:>3s} {:8.3s}" .format("n","Un"))
n=0
Un = 100                   
while Un>0:
   print("{:>3d} {:8.3f}".format(n, Un))
   Un = 1.01*Un - 1.01 
   n+=1
   
print("Foram mostrados:", n)