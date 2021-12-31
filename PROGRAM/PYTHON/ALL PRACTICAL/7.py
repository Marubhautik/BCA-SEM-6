#Create Simple set and Add value , remove Specific value(using discard and remove both function) ,Clear Set (using it's
#function).
a = {'bhautik','hitesh'}
print(a)
print("add value set")
a.add('dharmesh')
print (a)
print("remove specific value set")
a.remove('hitesh')
print(a)
print("discard value set")
a.discard('dharmesh')
print(a)
'''
{'hitesh', 'bhautik'}
add value set
{'hitesh', 'bhautik', 'dharmesh'}
remove specific value set
{'bhautik', 'dharmesh'}
discard value set
{'bhautik'}
'''
