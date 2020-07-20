# Exception hanling with basic use case scenarios

# 1) try/except block to take a value from the user and throw an exception if value is negative

def python_func1():
    try:
        input_value = int(input('Enter a Value: '))
        if input_value > 0 :
            print('Value is ', input_value)
        else:
            raise ValueError('Pass positive number...')
    except ValueError as val_err:
        print(val_err)
        
python_func1()

# 1a) Pass value = 5
    ''' 
        Input
            Enter a Value: 5
        Output
            Value is 5
    '''
    
# 1b) Pass value = -5
    '''
        Input
            Enter a Value: -5
        Output
            Pass positive number...
    '''
    
  
# 2) try/except/finally block to handle the exception

def python_func2():
    try:
        print(4/0)
        return 1
    except:
        print('Divide by zero exception')
        return 2
    finally:
        print('Executing Finally block')
        return 3
    
        '''
            Input
            Output
                Divide by zero exception
                Executing Finally block
                3
        '''