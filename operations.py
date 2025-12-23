x = 10                     #The first integer
y = 5                      #The second integer

print('Arithamatic Operation')    
       # Arithametic Operation
add = x+y                  #Adding two integers
sub = x-y                  #Subtraction two integer
mul = x*y                  #Multiplying two integers
div = x/y                  #Dividing two integers
squ = x**y                 # 5 is the power of 10
mod = x%y                  #Reminder of the division
flo = x//y                 #Nearest integer in the division
print(add)
print(sub)
print(mul)
print(div)
print(squ)
print(mod)
print(flo)

print('Assignment Operators')
        #Assignment Operators
x+=2                        #Here x = x+2
print(x)
x-=2                        # x = x-2
print(x)
x/=2                        # x = x/2
print(x)
x*=2                        # x = x*2
print(x)
x//=2                       # x = x//2 
print(x)
x%=2                        # x = x%2
print(x)
x**=2                       # x = x**2
print(x)

print('Comparison Operators')
        # Comparison Operators
equ = x == 10               # Equal 
neq = x != 10               # Not Equal
lth = x < 20                # Less then
gth = x > 20                # Grater then
geq = x >= 13               # Grater then or Equal
seq = x <= 13               # Less then or Equal
print(equ)
print(neq)
print(lth)
print(gth)
print(geq)
print(seq)

print('Logical Operators')
                #Logical Operators
print(x>11 and x<20)         # And logic operation
print(x<11 or x>20)          # Or logic operation
print(not(x<11 and x>20))    # Not logic operation

print('Identity Operators')
                #Identity Operators
x = ['apple','banana']       # First list
y = ['apple','banana']       # Second list
a = x                        # A = X
print(x is y)                # Even thow Thay have same elements in it . It shows False Thay are not Identitical
print(x is a )               # They are Identitcal because a=x
print(x is not y)            # For is not identical
print(x is not a)            # For is not identical
# There for is and == are not same
# Similar for is not and != also

print('Membership Operators')
            # Membership Operators
Fruits = ['apple','banana','mango','cherry']
print('cherry' in Fruits)        # To know cherry in the fruits list
print('hi'in Fruits)             # To know hi is in the list
print('pineapple' not in Fruits) # To conform wether pineapple in fruits list