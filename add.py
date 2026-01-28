from math import sqrt

def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n-1) + recur_fibo(n-2)

def main():
    nterms = 10

    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i))

    # formula-based fibonacci
    def nthFib(n):
        res = ((1+sqrt(5))**n - (1-sqrt(5))**n) / (2**n * sqrt(5))
        print(int(res), "is", n, "th fibonacci number")

    nthFib(10)

if __name__ == "__main__":
    main()
