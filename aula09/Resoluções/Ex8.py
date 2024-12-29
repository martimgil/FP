import sys
import math

def integrate(f, a, b, n):
   """The integral of f(x) for x between a and b.
   Aproximated using the trapezoidal rule with n uniform subintervals."""
   assert n >= 1
   h = (b-a)/n
   total = 0.5*(f(a)+f(b))
   for i in range(n):
      x_i = a + i*h
      total += f(x_i)
   
   return total*h


def example(n):
    """
    Calculate the integral of (x - 2) / (x + 3) from 0 to 3 using n subintervals.
    """
    def f(x):
        return (x - 2) / (x + 3)  # Define the function to be integrated
    
    result = integrate(f, 0, 3, n)
    return result



# Do not change the code below!
def evalPrint(expression):
    "Evaluate and print an expression and its result."
    result = eval(expression)
    print("{}\n--> {!r}".format(expression, result))

if __name__ == "__main__":
    evalPrint(" ".join(sys.argv[1:]))
