a = range(9)                  #This is the range command it counts from 0
print(a)                      #Showing the range
print(list(a))                #Converting the range to list

a = range(1,9)                #Giving the range from starting to end
print(list(a))                

a = range(1,9,2)              #The first number is start number and middle one is last and the last one is step of skip number
print(list(a))

for i in range(9):            #Here i will be counnting the range numbers
    print(i)

#We can also print like 
print(list(range(10)))
print(list(range(1,9)))
print(list(range(1,9,2)))
#To know wether it is in the range or not
print(5 in a)
print(4 in a)
#To know the length of the range
print(len(a))