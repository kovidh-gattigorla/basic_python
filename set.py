s = {'a','b','c','d','e','f','g','h'}                  #The set can have the data of alphabets but 'a' 
s1 = {1,2,3,4,5,6,7,8,9}                               #Set can have data of number
s2 = {1.0,1.1,1.2,1.3,1.4,1.5,1.6}                     #It can aslo have decimals
s3 = {'name','place','animal','thing'}                 #It can have 'words'
print(s)
print(s1)
print(s2)
print(s3)
                             #Access the set
for b in s:                                            #For finding the variable in set
    print('b is in s') 
    break                                              #Exit from the for loop
print(2 in s1)                                         #It shows the answer in the boolion
print('balance' in s3)                                 #Same
                             #Add the new element
s.add('i')                                             #For adding the new element
print(s)
s.update(s1)                                           #For updating the new set in old set 
print(s)
                             #Remove the set elements
s.remove('h')                                          #To remove selected elements
print(s)
s.discard('e')                                         #Alternate of removing the element
print(s)
a = s.pop()                                            #Poping or removing of first element storing in another variable
print(s)
print(a)
s.clear()                                              #Clearing the total set
print(s)
s = {'a','b','c','d','e','f','g','h'}                 
del s                                                  #Completely deleting the set
print(s)