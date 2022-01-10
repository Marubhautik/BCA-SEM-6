 #Enter the value from user and display the table of that value.
a = int(input("enter a number "))
print ("The Multiplication Table of: ", a)    
for count in range(1, 11):      
   print (a, 'x', count, '=', a * count)    
'''
enter a number 5
The Multiplication Table of:  5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''
