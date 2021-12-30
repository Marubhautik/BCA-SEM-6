#Create Simple list and Add value , Slice the value , remove Specific value ,
#Clear List (using i#t's function)
List=['bhautik','hitesh','dharmesh']
print(List)

print("add value list")
List.append('ali')
print(List)

print("Slice the value list")
List1=slice(4)
print(List[List1])

print("remove specific value list")
List.remove('ali')
print(List)

print("Clear List")
List.clear()
print(List)

'''
['bhautik', 'hitesh', 'dharmesh']
add value list
['bhautik', 'hitesh', 'dharmesh', 'ali']
Slice the value list
['bhautik', 'hitesh', 'dharmesh', 'ali']
remove specific value list
['bhautik', 'hitesh', 'dharmesh']
Clear List
[]
'''

