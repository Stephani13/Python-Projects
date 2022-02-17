


#create class
class Encapsulation:
    def __init__(self):
        #set the value of private and protected variables
        self._protectedVar = 34
        self.__privateVar = 2
    #add and retrieve the value
    def getVar(self):
        print(self._protectedVar + self.__privateVar)


#call to print results
enc = Encapsulation()
enc.getVar()
