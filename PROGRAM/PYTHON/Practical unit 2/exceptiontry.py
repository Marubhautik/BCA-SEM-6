try:
    a=int(input("Enter a :"))
    b=int(input("Enter b:"))
    c=a/b
    print("a/b = %d"%c)
except Exception:
    print("can't divide by zero")
    print(Exception)
else:
    print("Hi iam else block")

'''
Enter a :53
Enter b:0
can't divide by zero
<class 'Exception'>
'''