#oops -> object oriented programming structure
class nerd:
    #properties
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    #functions
    def displaydetails(self):
        print("details of nerd: ")
        print("name: ", self.name)
        print("age: ", self.age)
        print("hobby: ",self.hobby)

#creating object
s1 = nerd("john doe", 500, "sleeping")
s1.displaydetails()

s2 = nerd("micheal", 10e1000000000000000000000000000000000000000000000000000000000000000, "flying without plane")
s2.displaydetails()

s3 = nerd("goontwerp", "immortal", "sitting on the toilet")
s3.displaydetails()