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
print("this is my list =",mylist)
print("when you work with list you can extract the index you need from the list like this")
print("value of the first item =",mylist[0]) # the order of a list always start from 0 
# modify the element of a list
mylist[0]="4"
print("whit mylist[0]='4' i changed the value of the first item in the list, tha values of my list are =",mylist)
# add items to the list 
mylist.append("5")
print("using mylist.append('5') you can add a value '5' at the end of the list like this ", mylist)
mylist.insert(3,"6")
print("using mylist.insert(3,'6') you can add the value '6' at the position given (3) ,like this ", mylist)
# remove items from the list
mylist.remove("3")
print("using mylist.remove('3'), you can remove the value '3' from the list, like this ",mylist)
mylist.pop(0)
print ("with mylist.pop(0) you can remove the element of the list at the position given(0),like this ",mylist)
# append list
list2=["7","8","9"]
print("you can append a list to another one to have a bigger list, first create a new list called list2, list2=",list2)
mylist.extend(list2)
print("with mylist.extend(list2) you can add the value of list2 to mylist, mylist =",mylist)
#sort a list
mylist.sort()
print("whit mylist.sort() you can sort the elements of you list, mylist =",mylist)
mylist.sort(reverse = True)
print("with mylist.sort(reverse = True) you can sort your list with reverse order, mylist =",mylist)

# DICTIONARIES
# Dictionaries are collections key:value that are ordered , changeable and does not allow duplicates 
myDict= {name:"Giorgio", cognome:"Bianchi", anno_nascita:1992 }
print("this is a dictionary , myDict =", myDict)