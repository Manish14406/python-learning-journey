class Employee:
    
    def __init__(self,name,salary,):
        self.salary = salary   # create the instance attribute of name salary and assign it with salary
        self.name = name
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The employee name is {self.name} and her salary is {self.salary}")

havi = Employee("havi",200000)
print(havi.get_salary())
print(havi.get_info())


