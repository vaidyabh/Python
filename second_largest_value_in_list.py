############################################################################################################

#To find the second largest value in the list
#We have a list of the array and we compare the element one by one to find the second largest value in the list
############################################################################################################
#Initializing the list with some random numbers
list1 = [12, 45, 2, 41, 31]

#Assigning the initial value to the variables largest ans largest2
largest = largest2 = list1[0]

#iterating the loop from the 2nd to the last value to find the 2nd largest value in the list
for i in list1[1:]:
  if i > largest:
        largest2 = largest
        largest = i
  elif i > largest2:
        largest2 = i

#Printing the second largest value of the list
print('Second largest value in list : ', largest2)


#######################################################################################################################
Output:- Second largest value in list :  31
