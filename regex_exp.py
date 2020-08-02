#This file will contain the basic example of the regex expression

'''
    Regex helps in pattern search, find and replace, manipulate text
    Regex can be used on the data stored in the files or the variables that are processing on run time
'''
'''
    *  -- Match 0 or more occurance
    +  -- Match 1 or more occurance
    .  -- Match all character except new line
    ?  -- Match 0 or 1 occurance
    [] -- Match the range
    \
'''
#Improting the lirararies
import re

# 1) Print the string separated by the / in the string

python_string = 'test/file/location/data'
 
# 2) Print the string 
  re.search(r'(.*)/(.*)', python_string).group(0)
  '''
      OUTPUT: 'test/file/location/data'
  '''


# 3) Print the string before last /
  re.search(r'(.*)/(.*)', python_string).group(1)
  '''
      OUTPUT: 'test/file/location'
  '''


# 4) print the last data after last /
  re.search(r'(.*)/(.*)', python_string).group(2)
  '''
      OUTPUT: 'data'
  '''


# Search if a character or the pattern exists in the string
# 5) Find / in the string named search_string

 search_string = 'test/file/location/data'

if '/' in search_string:
    print(True)
else:
    print(False)


'''
      OUTPUT: True
  '''



if '/' in search_string:
    print(True)
else:
    print(False)
    
   
'''
      OUTPUT: False
  '''
   



# 6) Search and print the first occurance of the digit from the list

list1 = [123, 222, 'abcde', 'abc4de', 'aa5', '622b']
pattern = re.compile('[0-9]')
for value in list1:
    pm = pattern.search(str(value))
    if pm:
        print(pm.group())
        
        
'''
    OUTPUT:
        1
        2
        4
        5
        6
'''

# 7) Find all the digits from the given list
list1 = [123, 222, 'abcde', 'abc4de', 'aa5', '622b']
pattern = re.compile('[0-9]+')
for value in list1:
    pm = pattern.search(str(value))
    if pm:
        print(pm.group())
        
'''
    OUTPUT:
        123
        222
          4
          5
        622
'''
        

# 7) Find first alphabet from the list
list1 = [123, 222, 'abcde', 'abc4de', 'aa5', '622b']
pattern = re.compile('[a-zA-Z]')
for value in list1:
    pm = pattern.search(str(value))
    if pm:
        print(pm.group())
        
'''
    OUTPUT:
        a
        a
        a
        b
''' 
