d = {'name':'python','clas':'b.tech','rank':1}
d1 = {'name':'java','clas':'b.tech','rank':[1,2]}                         #We can also store the list in it
d2 = dict(name='c', clas='b.tech', rank=[1,2,3])
print(d)                                                                     
print(d1)
print(d2)
print(type(d))                                                             #Type is Dictionarie
print(len(d))
                                    #Accessing the dictionaries
print(d['name'])                                                           #It is like name = python if we print name then python or voice versa
a = d1.get('rank')                                                         #by takig the element and get 
print(a)
b = d1.keys()                                                              #The left side elements of : are keys
print(b)
c = d2.values()                                                            #Richt side elements are vlaues
print(c)
d = d.items()                                                              #Every thing menctioned is item
print(d)
if 'rank' in d1:                                                            #If condition
    print('Yes it is True')