'''
    class is used to create a collection of functions and variables for a specific purpose 

    Summary
    - creating Robot class 
    - creating constructor
    - viewing variables  
    - function variable default value 
    - class function 
    - static function 
    - updating instance variables with set function 
    - static variable 


    https://dotnettutorials.net/lesson/class-variables-in-python/#:~:text=Types%20of%20Class%20Variables%20in%20Python%3A&text=They%20are%3A,Local%20variables
'''
class Robot: 

    # class variable shared by all instances 
    everyRobotHasThis = 'a heart'

    # constructor
    # can also have default variables if none are passed in 
    def __init__(self,name,howCool='very cool'): 
        self.__name  = name # can use __ to show it's private since python only have public variables 
        self._howCool = howCool

    '''
        IF you forget the self and do robot.doSomethingCool, you will get an error
    '''
    def doSomethingCool(self): 
        print(self._name, 'lifts right eyebrow and winks ;)')

    # static method (don't need to pass in self)
    # static method can be called without instantiating the object 
    def tooCoolToInstantiate(): 
        print('I am special. Who needs an object?')

    def setName(self,newName): 
        self.__name = newName
    # if no return statement where, will return nothing by default 

    def getName(self): 
        return self.__name

# instantiating the class object 
myRobot = Robot('Kevin')


'''
    can see what's inside robot and the variables 
'''

'''
    to see the name can do 
    myRobot._Robot__name 
    > 'Kevin' 

'''
myRobot.doSomethingCool() 

# calling static method 
Robot.tooCoolToInstantiate() 

# can see both robot have the same the variable 
# create second robot
myRobot2 = Robot('John')

'''
    myRobot.everRobotHasThis 
    > 'a heart' 

    myRobot2.everRobotHasThis 
    > 'a heart'

    see the same output 
'''

'''
    ways to update instance variable 
'''
myRobot.getName() 
myRobot._Robot__name = 'John'
myRobot.getName()
myRobot.setName('kevin')
myRobot.getName() 


'''
    can update class variables outside of class 
    notice the everyRobotHasThis variable will update 
'''
myRobot.everyRobotHasThis
myRobot.everyRobotHasThis = 'cpu'
myRobot.everyRobotHasThis

debug = 1 