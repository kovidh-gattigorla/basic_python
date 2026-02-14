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