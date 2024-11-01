# Print a multiplication table like this:
#   1 x 1  =   1
#   1 x 2  =   2
#   ...
#  10 x 10 = 100
#
# Make the program print an empty line after each group of ten.
# Also, use format specifiers to align the numbers.
#
# JMR 2019
def multiplication():
    for first in range(1,11):
        for second in range(1,11):
            valor = first*second
            print("{:>4d} x {:<3d}={:>4d}".format(first, second, valor))
        print()



if __name__ == "__main__":
    multiplication()