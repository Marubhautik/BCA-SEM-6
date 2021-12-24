#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
   print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

'''
I am from Sweden
I am from India
I am from Norway
I am from Brazil
'''
