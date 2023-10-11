'''
    1. base class 
    2. inherited class 
    3. constructor for inherited class and updating base class variables 
    4. abstract methods that will be overwritten, different behavior for different inherited class 
    5. accessing variables belonging to base and derived classes 
'''
class Robot: 

    def __init__(self,name,id):
        self.__name = name
        self.__id = id 

    # function shared by all subclasses 
    def printName(self):
        print('my name is:',self.__name)


    # @abstractmethod 
    def doSomething(self): 
        return


class CoolRobot(Robot): 
    def __init__(self,name,id,coolnessLevel): 
        super().__init__(name,id)
        self.__coolnessLevel = coolnessLevel

    def doSomething(self):
        print(self._Robot__name,'raise eyebrow')

class BoringRobot(Robot): 
    def __init__(self,name,id): 
        super().__init__(name,id)

    def doSomething(self):
        print(self._Robot__name,'zzzzzz')

myCoolRobot = CoolRobot('kevin',10,1000)

# can access variable of derived class 
myCoolRobot._CoolRobot__coolnessLevel

# can also access variables of base class 
myCoolRobot._Robot__id

myCoolRobot.printName() 
myCoolRobot.doSomething() 

myBoringRobot = BoringRobot('john',100)
myBoringRobot.printName() 
myBoringRobot.doSomething() 

debug = 1 