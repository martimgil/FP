# This program shows a table of the squares of four numbers.
# Modify the program to show the squares of 1..20.  Use the range function.
# Also, add a column to show 2**n.  Adjust the formatting.

print("{:>5s} {:>5s} {:>10s}".format("n", "n²", "2**n"))
for n in range(21):
    print("{:>5d} {:>5d} {:>10d}".format(n, n**2, 2**n))
