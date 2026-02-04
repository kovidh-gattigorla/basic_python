# This is the list
a = ['a','b','c','d']              #This is the List of strings
b = [1,2,3,4,5,6,7,8,9]            #This is the List of int

                 # Accessing the list
print(a[-1])                       #The -1 comes from last in the list
print(a[2])                        #In list it will start form 0 so 2 is c
print(a[1:3])                      #This will start from b to d
print(a[:2])                       #This will end at 2 means c
print(a[2:])                       #This will start from 2 means c to end
print(a[-3:-1])                    #This will be counting from to -3 'b' to 1 'd'

                 # Changeing the list
a[2]='a'                           #Changed the value of 'a' with the 'c'
print(a)                

a[2:3] = 'b','c'                   #Changed the values of 'c' to 'b' and 'd' to 'c'
print(a)
                 # Adding the new list
a.insert(4,'e')                    #Inserting the e in 4 position
print(a)

a.append('f')                      #Adding the given input f at the end 
print(a)

a.extend("g")                      #Extending the list with g
print(a)
             #Remove elements in the list
a.remove('b')                      #To remove the Element in List
print(a)

a.pop()                            #Pop is used for poping or removing the Element in List
print(a)  

del a[-1]                          #del for deleting 
print(a)

a.clear()                          #Clearing all the Element
print(a)      
                #Loop in the List
if 3 in b :                      #We can use the if condition in the list
    print(3)   

for i in range(len(b)):          #To split the list supperatly
    print(b[i])
i = 0                            #It is took that imaganary=0    

while i<len(b):                  #While the imaganary is less and len of b is grater
    print(b[i])                  #Printing the list and the value of i element
    i=i+1                        #i=0 and i=0+1 and i=1+1 until the end i=7+1
[print(x)for x in b]             #The x is a value so elements in the b list
                      #Sort List
a = ['c','d','a','b']            #created teh new list        

a.sort()                         #It will be arranging the list order in the alphabitical order
print(a) 

a.sort(reverse=True)             #It will be doing revers of the sorting
print(a)

a.reverse()                      #Just reversing the data of alphabitical order
print(a)

a = ['C','D','a','b']

a.sort(key=str.lower)            #It will be sotring the insensitive data
print(a)

def lists(n):
    return abs(n-10)             #Returning the nearest values of 10
c = [50,20,11,9,6,17,22,5,1]  
c.sort(key=lists)                 #Using the functin in the sort key
print(c)
                   #Copy the List
a = ['apple','banana','cherry','pinapple','guava']

fruit = a.copy()                 #Copying the lsit 
print(fruit)

frutis = list(a)                 #Copying the list with the List method
print(frutis)

frut = a[:]                      #We can also copy the list with the :
print(frut)
                   #Adding 2 List

l1 = ['a','b','c','d','e','f']
l2 = [1,2,3,4,5,6]
l3 = l1+l2                       #Adding the list in the Arthamatic operation
print(l3)

for x in l2:
    l1.append(x)                 #By using the append command for adding
print(l1)

l1.extend(l2)                    #Extending the list by extend command
print(l1)


