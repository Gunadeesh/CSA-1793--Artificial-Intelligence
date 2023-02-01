iList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# List slicing operations
# printing the complete list
print('iList: ',iList)
# printing first element 
print('first element: ',iList[0]) 
# printing fourth element 
print('fourth element: ',iList[3]) 
# printing list elements from 0th index to 4th index
print('iList elements from 0 to 4 index:',iList[0: 5]) 
# printing list -7th or 3rd element from the list
print('3rd or -7th element:',iList[-7])
# concatenation of two lists  
# declaring the lists  
ilist1 = [12, 14, 16, 18, 20]
print('ilist1: ',ilist1)
ilist2 = [9, 10, 32, 54, 86]
print('ilist2: ',ilist2)
# concatenation operator +  
l = ilist1 + ilist2  
print(l)
# size of the list  
# declaring the list  
ilist3 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
print('ilist3: ',ilist3)
# finding length of the list  
print("Total Elements: ", len(ilist3))    
# iteration of the list  
# declaring the list  
ilist4 = [12, 14, 16, 39, 40]
print('ilist4: ',ilist4)
# iterating  
for i in ilist4:   
    print(i)
ilist5 = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print('ilist5: ',ilist5)
print(ilist5[2])
# Prints ['cc', 'dd', ['eee', 'fff']]
print(ilist5[2][2])
# Prints ['eee', 'fff']
print(ilist5[2][2][0])
# Prints eee
