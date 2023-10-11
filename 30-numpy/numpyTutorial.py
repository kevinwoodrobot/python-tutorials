'''
    pip install numpy 
    running in virtual env 

    Summary - numpy is a module good for dealing with arrays, 
    math functions, linear algebra, and basic statistics 
'''
import numpy as np 

'''
    function: array - 1d or 2d matrix 
    paramter: 
        - elements: list for 1d array OR list of list 
'''
A = np.array([1,2,3])
A = np.array([[1,2,3],[4,5,6],[7,8,9]])

'''
    matrix.shape: size of array 
    returns: tuple 
'''
print(A.shape)

'''
    indexing
'''
print(A[2][2]) # specific element
print(A[0:2,0:2]) # submatrix 

'''
    function: arange - list of numbers spaced with step size, 
        number of points calculated  
    parameter: 
        start 
        stop 
        nStep
'''
A = np.arange(1,10,2)

'''
    function: linspace - list of numbers with number of points, 
        step size calculated 
    parameter: 
        start 
        stop 
        nPoints  

'''
A = np.linspace(1,10,4)

'''
    common math functions trig functions, log, exp 
        - can get value at one input 
        - or get value for range of inputs 
'''
A = np.cos(1)
A = np.cos(np.arange(0,1,.1))

'''
    function: zeros - matrix of zeros 
    parameter: 
        size - tuple for rectangular or square OR
               int for 1d array 
'''
A = np.zeros((2,3))
A = np.zeros(5)

'''
    function: ones - matrix of ones 
    parameter: 
        size - tuple for rectangular or square OR
               int for 1d array 
'''
A = np.ones((2,3))
A = np.ones(5)

'''
    function: full - matrix filled with one number 
    parameter: 
        size - tuple or int 
        number - float
'''
A = np.full((2,3),10)
A = np.full(2,10)

'''
    function: eye - identity matrix 
    parameter: 
        size - int, always square matrix 
'''
A = np.eye(3)


'''
    function: random.rand - matrix of random number 
    paramters 
        size with variable inputs...(d0,d1,d2,...)
             - one input, 1D 
             - two inputs, 2D 

    use random.randn for normal distribution 
'''
A = np.random.rand(2)
A = np.random.rand(2,3)

'''
    function: transpose 
    parameter: 
        matrix - np array 
'''
A = np.random.rand(2,3)
A = np.transpose(A)

A = np.array([1,2,3]) 
A = np.transpose(A) # transpose is unchanged for 1d array!!!, need reshape 

'''
    function: reshape
    parameter: 
        matrix - np array 
        size - tuple 
'''
A = np.reshape(A,(3,1))

'''
    function: dot 
    parameter: 
        matrix1 - np array
        matrix2 - np array 
'''
B = np.array([1,2,3])
A = np.dot(B,B)

'''
    function: matmul - matrix multiply 
    parameter: 
        matrix1 - np array
        matrix2 - np array 

    Also can do B@B 
'''
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
A = np.matmul(B,B)
A = B@B

'''
    function: linalg.inv - inverse of matrix 
    parameter: 
        matrix - np array 
'''
B = np.random.rand(3,3)
A = np.linalg.inv(B)

'''
    function: eig - eigenvalue of matrix 
    parameter: 
        matrix - np array 

'''
A = np.linalg.eig(B)

'''
    some basic stats functions 

    can check gaussian distribution by finding the average of randn 
    randn mean of 0, distribution of 1
'''
B = np.random.randn(100)
A = np.average(B)
A = np.min(B)
A = np.max(B)
np.
print(A)

# u,s,vh = np.linalg.svd(B)
# print('u',u)
# print('s',s)
# print('vh',vh)

# S = np.diag(v=s)
# print('B',u@S@vh)
# print('B',B)

