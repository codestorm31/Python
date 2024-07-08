class Employee:
    language="Python"
    salary=1200000

    def __init__(self,name,salary,language): # dunder method is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"Name is {self.name}, Language is: {self.language} & salary is:{self.salary}")
        
emp1=Employee("Aryan",1300000,"C++")
emp1.getInfo()