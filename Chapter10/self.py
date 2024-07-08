class Employee:
    language="Python"
    salary=1200000

    def getInfo(self):
        print(f"Language is: {self.language} & salary is:{self.salary}")
        
emp1=Employee()
emp1.getInfo()