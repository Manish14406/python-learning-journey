# class student:
#     def __init__(self,name,cls):
#         self.name = name                    #initialization of cls objects
#         self.cls = cls
#     def display(self):
#         print(f"Name  : {self.name} \nClass : {self.cls}")

# s1 = student("Manish",4)  # creating obj
# s1.display()   #calling display method

#Built in functions

# class Manish:
#     def __init__(self,name,cls):
#         self.name = name
#         self.cls= cls
# H = Manish("haviii",6)
# print(getattr(H,'name'))
# setattr(H,'name','rudie')
# print(hasattr(H,'name'))
# delattr(H,'name')



#polymorphism 
# class Dog:
#     def sounds(self):
#         print("Bow")
# class Cat:
#     def sounds(self):
#         print("meow")

# for animals in Dog(),Cat():
#     animals.sounds()

# inheritance - it is a property where child class inherits the properties of parent class

# class vehicle:
#     def speed(self):
#         print("Vehicle over speed")

# class Car(vehicle):
#     pass
# C = Car()
# C.speed()

#abstraction hiding the internal details and showing the essential feature

a = input("enter")
