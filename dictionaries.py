d = {'name':'python','clas':'b.tech','rank':1}
d1 = {'name':'java','clas':'b.tech','rank':[1,2]}                         #We can also store the list in it
d2 = dict(name='c', clas='b.tech', rank=(1,2,30))                         #We can also store the list in it
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
                                     #Changeing Item
d1['rank']=3                                                               #Changing the value
print(d1)
d1.update({'rank':10})                                                     #Changed by update
print(d1)
                                     #Adding Item
d1['type']='easy'                                                          #Added the new key and value
print(d1)
d1.update({'level':10})                                                    #Added by update
print(d1)
                                     #Remove Item
d1.pop('name')                                                             #Pop ping the item                      
print(d1)
d1.popitem()                                                               #Last item will be removed
print(d1)
del d1['rank']                                                             #Deleting the item menctioned
print(d1)
d1.clear()                                                                #Total dicitonarie is cleared
print(d1)
                                     #Loop in dictionarie
for x in d2:                                                              #For x in every element of the dictionarie
    print(x)
    print(d2[x])                                                          #Here it will be printing the keys
                #OR
for x in d2.values():
    print(x)
for x in d2.keys():
    print(x)
for x in d2.items():
    print(x)
     