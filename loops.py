# For Loop
for x in range (9):               #Heare the x is having the range of 9 from 0 to 8  
    print(x)                         
                 
for x in range (2,9):             #Here the x range is from 2 to 9
    print(x)

for x in range (1,10,2):          #Here the range is from 1 to 10 and it will be skiping 2 numbers
    print(x)

week = ['monday','thusday','wednesday','thursday','friday','saturday','sunday']            #This loop will also work for the list
for a in week:                    #a is said to be the week list
    print(a)                      
    if a == 'wednesday':          #Conditions are also can be used
        break                     #This will break the loop where you want

# While Loop
x = 1
while x<10:                       #Here it will be looped until the value reach the given number
    print(x)
    x +=1

x = 1
while x <6 :                      #This will never going to end
    print(x)
    x +=1
    if x == 5 :
        break                     #This break will break the loop
