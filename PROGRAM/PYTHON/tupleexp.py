t = (5,'program', 1+3j)
print("t[1] = ", t[1])
print("t[0:3] = ", t[0:3])
t[0] = 10

'''
OUTPUT

t[1] =  program
t[0:3] =  (5, 'program', (1+3j))
Traceback (most recent call last):
  File "D:/Bhautik/tupleexp.py", line 4, in <module>
    t[0] = 10
TypeError: 'tuple' object does not support item assignment
'''
