Tuple1 = ()  
print("Initial empty Tuple: ")  
print (Tuple1)  
  
Tuple1 = ('King', 'For')  
print("\nTuple with the use of String: ")  
print(Tuple1) 
  
list1 = [1, 2, 4, 5, 6]  
print("\nTuple using List: ")  
print(tuple(list1))  
  
Tuple1 = tuple('King')  
print("\nTuple with the use of function: ")  
print(Tuple1)  
 
Tuple1 = (0, 1, 2, 3)  
Tuple2 = ('python', 'king')  
Tuple3 = (Tuple1, Tuple2)  
print("\nTuple with nested tuples: ")  
print(Tuple3)

# OUTPUT
#Initial empty Tuple: 
#()

#Tuple with the use of String: 
#('King', 'For')

#Tuple using List: 
#(1, 2, 4, 5, 6)

#Tuple with the use of function: 
#('K', 'i', 'n', 'g')

#Tuple with nested tuples: 
#((0, 1, 2, 3), ('python', 'king'))
