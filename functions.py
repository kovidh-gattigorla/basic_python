def Hello_world():                            # Starting of the function with the 'def'
    print('hello world')                      # What is in the function
Hello_world()                                 # End of the function

def hay(name):
    print(name +' Hello')
hay('Sham')                                   # We can use the function multiple times
hay('Ram')                                    # This is aslo one reason for using function
hay('Vanki')

def my_function():                            # This is the first function
    x=100                                     # Input is in the first function
    def inner_function():                     # This is inner function
        print(x)                              # The result is in the inner function
    inner_function()
my_function()