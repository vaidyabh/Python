''' This python will help in passing the multiple arguments with and without using named parameters'''
 
 '''
    unapacking method is useful in python, can be used if need to pass the number of variables which are dynamic in nature.
    Make code more robust to read and debug
'''

# Reading variables from tuple

# This function will throw an error if the number of the arguments are more than 1
def read_tuple(args):    
    print('args in tuple', args)

read_tuple(1)                # args in tuple 1
read_tuple(1,2,3)            # TypeError: read_tuple() takes 1 positional argument but 3 were given

# Use * with args to avoid the limitation of number of variables
def read_tuple(*args):    
    print('args in tuple', args)
    for var in args:
        print(var)

read_tuple(1,2,3)             # args in tuple (1, 2, 3)
read_tuple((1,2,3))           # args in tuple ((1, 2, 3),) return tuple of tuple

 
'''
# Output
    args in tuple (1, 2, 3)
    1
    2
    3
    args in tuple ((1, 2, 3),)
    (1, 2, 3)
'''

# Reading variables from list

def read_list(*args):
    print('args in list', args)
    for var in args:
        for list_var in var:
            print('List var : ',list_var)

read_list([1,2,3])


'''
# Output
    args in list ([1, 2, 3],)
    List var :  1
    List var :  2
    List var :  3
'''


# Reading variables from dictionary

# Read only keys from dictionary
def read_dict(*args):
    print('args in dict', args)
    for key in args:
        print(key)
 
read_dict(*{"x" : 1, "y" : 2})


'''
# Output

    args in dict ('x', 'y')
    x
    y

'''


# Add the multiple variables without defining the number of variables to be added
def add(*args):
    total = 1
    print(args)
    for var in args:
        total = total + var
    return total

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))

'''
Output
    (1, 2)
    4
    (1, 2, 3)
    7
    (1, 2, 3, 4)
    11

'''

# Add the multiple variables without defining the number of variables to be added
def mul(*args):
    #print(args)
    total = 1
    for var in args:
        total = total * var
    return total

print(mul(1,2,3))
print(mul(1,2,3,4))

'''
Output

    6
    24
'''

#Main function to call the functions to perform the airthmatic operations
def main(*args, func):
    if func == '+':
        #return add(args) --- will throw an error, args will be (1,2,3) i.e. tuple instead of the values.
        #                     Need to pass * with the args to read the variables from the tuple
        return add(*args)
    if func == '*':
        return mul(*args)

print(main(1,2,3, func = '*'))
print(main(1,2,3, func = '+'))


'''
Output
    6
    (1, 2, 3)
    7
 '''