import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
try:
    linux_interaction()
except:
    pass
try:
    linux_interaction()
except:
    print("Linux function was not executed")

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("The linux_interaction() function was not executed")

'''
Linux function was not executed
Function can only run on Linux systems.
The linux_interaction() function was not executed
'''

