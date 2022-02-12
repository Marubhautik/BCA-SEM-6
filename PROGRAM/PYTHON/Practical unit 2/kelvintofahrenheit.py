def ktof(tem):
    assert (tem>=0),"Colder than absolute zero!"
    return ((tem-273)*1.8)+32
print(ktof(273))
print(int(ktof(505.78)))
print(ktof(-5))
''' 
 File Practical unit 2/kelvintofahrenheit.py", line 2, in ktof
    assert (tem>=0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
32.0
451
'''