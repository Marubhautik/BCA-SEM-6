# WAP to Perform all the arithmetic operation if value is negative the Display the Message "Please Enter Proper Value..." and
#Get The Value

a= int(input("Enter a number"))
b= int(input("Enter a second number"))

if(a>0 and b>0):
    print('''
1. addtion
2. substraction
3. multiplication
4. division
''')
    c=int(input("please select option"))
    if(c==1):
        print("adition:",a+b)
    elif(c==2):
        print("substraction:",a-b)
    elif(c==3):
        print("multiplication:",a*b)
    elif(c==4):
        print("division",a/b)
    else:
        print("invalid selection")
else:
    print("Please Enter Proper Value...")
'''
Enter a number-8
Enter a second number8
Please Enter Proper Value...
'''
