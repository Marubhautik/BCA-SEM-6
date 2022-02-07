def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print("Fibonacci number 10:-",fib(10))
'''
Fibonacci number 10:- 55
'''
