# references 
# https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
# https://flexiple.com/python/python-print-variable/



# print with single quotes 
print('single quotes')

# print with double quotes 
print("double quotes")

## print with variables 
num1 = 1 
num2 = 3.234

# print with comma 
print('my number is ', num1)

#print single variable with string formatting operator 
print ('my number is %d' %(num1) )
print('my number is %.2f' %(num2))

# print more than one variable with string formatting operator 
print('my numbers are %d and %d' %(num1, num2))

# print with f-string 
print (f'my numbers are {num1} and {num2}')

# print with string concatenation 
# print('my number is ' + num1) # error, num1 is not string
print('my number is ' + str(num1))

# print format method 
print('my number is {}' .format(num1))
