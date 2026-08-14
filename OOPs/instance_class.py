class couple:
    wife = "havi" # this is class attribute 
    
    def __init__(self,name,wife,contact):
        self.name = name
        self.wife = wife
        self.contact = contact

    def info(self):
        print(f"Manish's wife is {self.wife} and her contact number is {self.contact}")

c1 = couple("Manish","havyashree",12123)
print(c1.info())  # it will always print instance attribute whenever it is present 
print(couple.wife) # prints the class attribute

# object introspection  - way to find all the methods and attributes that a particular object in python has 
print(dir(c1))

