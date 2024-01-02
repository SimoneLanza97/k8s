# THIS IS A PYTHON SCRIPT MADE TO SEE HOW CAN YOU USE PYTHON TO MANAGE DATAS

# print values
print("with print(), you can print at screen what you want!")

'''creating a variable 
you can just write VARIABLE_NAME = VALUE'''

x = 5
print("the value of x is", x )  # text between "" , values of variables outside "" , the ',' is a delimiter 

'''but variables can be strings , integers , floats or boolean and you can declare
the type or see what type of data there is inside a variable whit tipe(var)'''

y = str("my name is")
z = bool(0)

print("the values of x y and z are", "x=",x,"y=", y,"z=", z , ", and their types are", type(x), type(y), type(z))

''' In pyhton strings are arrays , ararys of caracters and you can manage them like arrays 
but , how can you manage arrays? 
you can :
    - append arrays 
    - modify arrays 
    - add and remove indexes from array
but in python we don't use arrays properly , we use list , that are something very similat to the arrays '''

mylist=["1","2","3"]
print("this is my list=",mylist)
print("when you work with list you can extract the index you need from the list like this")
print("value of the first item=",mylist[0]) # the order of a list always start from 0 

