# String input
name = input('Your name:')                 #To input a string are any symbol
print('Hello '+name)                       #For the input comand '+' should be there

# Int input
a = int(input('Your age:'))                #To input the integer int(input)is used
print('Your age is ',a)                    #It is not like string so ','is enough

# Float input
a = float(input('Enter the GPA:'))         #To input the float float(input)
print('Your GPA is ',a)                    #It is like int so ','.Reentred numbers or not taken

# List input
l = list(input('Enter the elements:'))     #This is for list so list(input) for input space are also counted
print('List are :',l)                      #This are mixed or floats so ','.Reentred numbers or not taken

# Tuple input
t = tuple(input('Enter the elements:'))    #This for tuple so tuple(input) . in input space and gapes are counted
print('Tuple are :',t)                     #This is mixed so ','.Reentred numbers or not taken

# Set input
s = set(input('Enter the elements: '))     #This is for the set(input).here spaces are counted as elements
print('Set: ',s)                           #This is mixed so ','.Reentred numbers or not taken

# Dictionary input
d = input('Enter the elements: ')          #This is for the dictionary
words = {word:len(word) for word in d.split()} # This line is for making the second element as the dictionary
print(words)                               #Re-entred numbers or not taken