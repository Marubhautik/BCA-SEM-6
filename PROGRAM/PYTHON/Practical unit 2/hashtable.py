def hash_key( key, m):
    return key % m

m = 7

print(f'The hash value for 3 is {hash_key(3,m)}')
print(f'The hash value for 2 is {hash_key(2,m)}')
print(f'The hash value for 9 is {hash_key(9,m)}')
print(f'The hash value for 11 is {hash_key(11,m)}')
print(f'The hash value for 7 is {hash_key(7,m)}')

'''The hash value for 3 is 3
The hash value for 2 is 2
The hash value for 9 is 2
The hash value for 11 is 4
The hash value for 7 is 0'''