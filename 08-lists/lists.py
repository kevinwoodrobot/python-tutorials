# declaring a list 
stringList = ['kevin','robot'] # string only 
intList = [3,2,5] # ints only 
mixedList = ['kevin',1,'robot',2] # combine different data types 
listOfList = [[1,2,3],[4,5,6],[7,8,9]] # list of list, good for 2d arrays 

# indexing list, same way as indexing strings 
mixedList[0:1] # first 
mixedList[0:2] # first two 
mixedList[0::2] # [first:last:step] every other


# list functions 
mixedList.append('python')
mixedList.clear() # clears the items inside the list 

'''
    wrong way of making copying for a list 
'''
# will point to the same list. Modifying tempList will also modify mixedList
mixedList = ['kevin',1,'robot',2] 
tempList = mixedList  # mixedList = ['kevin',1,'robot',2]
tempList[0] = 'john' 
# mixedList = ['john',1,'robot',2], noticed mixedList is now changed 
# tempList = ['john',1,'robot',2], same output because pointing to the same list 

'''
    correct way of making copy for a list 
'''
# if you don't want to modify the original list, need to make a copy 
mixedList = ['kevin',1,'robot',2] # reinitialize to original list
tempListCopy = mixedList.copy() # make a copy
tempListCopy[0] = 'john' 
# mixedList = ['kevin',1,'robot',2], unchanged as expected because tempListCopy is not pointing to mixedList
# tempListCopy = ['john',1,'robot',2], 


mixedList.pop() # will remove last element, treating list as a stack 
mixedList.insert(5,'blah') # will insert 'blah' at 5th element (zero index not applied) 
mixedList.remove('blah') # will remove blah from mixedList 
intList.sort() # will sort intList, but not different data types like in mixedList


debug = 1 