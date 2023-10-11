myString = "kevin is not a robot"

# a long string in one line, typed out in more than one line
longString = 'asdfsdfsdfsdf '\
    'dasdfsfsfsda'

# a string spaning multiple lines 
multiLineString = '''sfjksaljfs 
kasjdflkjsl'''

# a string spanning multiple lines 
# using escape charcter \n 
multiLineString2 = 'asdfsadfs \n'\
    'asdfsdfasdfsd'

myString[0]
myString[0:3]
myString[5:]
myString[:5]

# concatenate strings
theTruth = myString[0:8] + myString[9+3:]

## string functions examples 
# can see function by typing string name and '.' in python script 
# a drop down menu should appear 

# split strings 
maxSplit = 2 
# default is None, meaning splits at any 
myString.split() # split will split strings from the lift 
myString.rsplit(None,maxSplit) # rsplit will split string from the right 
myString.count('kevin')

myString.isdecimal()

myString.upper()

debug = 1 