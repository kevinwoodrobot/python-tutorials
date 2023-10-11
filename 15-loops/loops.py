# for loops 

healthyFoods = ['walnuts','avocados','dark chocolate']

# pythonic way 
for i in healthyFoods: 
    print(i)

# typical way 
for i in range(len(healthyFoods)): 
    print(healthyFoods[i])

# double for loop 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)): 
    for j in range(len(matrix[0])):
        print(matrix[i][j])


# while loop 
i = 1 
while i < 10: 
    print(i)
    i += 2


# infinite loop
i = 1 
while True: 
    print(i,'get me out')
    if i == 50: 
        break 
    i += 1 

    