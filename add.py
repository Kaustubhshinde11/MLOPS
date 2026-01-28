# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))





# To find the n-th Fibonacci Number using formula
from math import sqrt 
# import square-root method from math library
def nthFib(n):
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    # compute the n-th fibonacci number
    print(int(res),'is',str(n)+'th fibonacci number')
    # format and print the number
    
# driver code
nthFib(12)

# This code is contributed by Kush Mehta