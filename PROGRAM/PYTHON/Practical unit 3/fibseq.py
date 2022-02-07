def fib(n):  
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def all_fib(n):  
    fibs = []
    for i in range(n):
        fibs.append(fib(i))
    return fibs
print(all_fib(10))
'''
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
