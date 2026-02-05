t = (1,2,3,4,5,6,7,8,9)                             #In tuple we can enter integets but in ()
t1 = ('a','b','c','d','e','f','g')                  #We can also enter alphabets ('')
t2 = ('name','place','animal','thing')              #We can also use the ('words')
t3 = (1.0,1.1,1.2,1.3,1.4,1.5,1.6)                  #Float can aslo be used
print(t)
print(t1)
print(t2)
print(t3)

print(len(t))                                       #To find the length
print(type(t1))                                     #To find the Type 

                    #Accessing the Tuple
print(t[1])                                         #Giving the output of 1 element in the tuple . starts from 0
print(t[-1])                                        #Counting from last
print(t[:5])                                        #Prints every element from starting to 5
print(t[4:])                                        #Accesing every element after 4
print(t[2:6])                                       #Accessing the elements between the elements not count(2):(6)not counts
print(t[-6:-1])                                     #Accesing the elements from -6 to -1 (menction reversly wile using '-')
print(t[1:8:2])                                     #simelat with first 2 the last :2 will ne count after every 2

for thing in t2:                                     #Checking the Existency
    print('exist')
    break