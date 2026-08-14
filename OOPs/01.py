# OOPS- object oriented programming consists of class and object
# Advantages of oops
# -organisation
# -reuseability
# -easy to debug
# -real world modeling

# Four pillors of oops
# Abstraction    
# Encapsulation  
# Inheritence 
# Polymorphism -same methof name but different behavior in diff objects 

# class - blueprint (template) Ex: form for an exam that conatains name,age,class,address these kind of details 
# object - spcific instance created from the template(class) Ex: form which contains the data for  manish 
# if car is the class then honda civic is the object 
# -------------------------------------------------------------------------------------------------------------

# example 

class Employee:
    company = "google"

    def sal_month(self): # self is the way to reference the object of the class which is being created 
        print(self)
        return 200000
    

manish = Employee()        # An object of class Employee is created   
print(manish.sal_month())  # the method sal_month of manish is called 
print(manish.company)