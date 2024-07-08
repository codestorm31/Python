'''
1. Create a class “Programmer” for storing information of few programmers
working at Microsoft.
'''

class Programmer:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
        
    def __str__(self):
        return f"{self.name}, {self.age} & {self.role}"
    
p1=Programmer("Aryan",21,"SDE-I")
p2=Programmer("Avi",24,"Intern")

print(p1)