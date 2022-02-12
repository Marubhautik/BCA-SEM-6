try:
    print("try block")
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    z=x/y
except ZeroDivisionError:
    print("except zerodivisionerror block")
    print('division by 0 not accepted ')
else:
    print('else block')
    print("division=",z)
finally:
    print("finally block")
    x=0
    y=0
print("Out of try,except,else and finally blocks.")
'''try block
Enter a number:20
Enter another number:2
else block
division= 10.0
finally block
Out of try,except,else and finally blocks.'''