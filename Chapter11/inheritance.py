class employee:
    comp="ITC"
    def show(self):
        print(f"The name is {self.name} & salary is {self.salary}")
        
# class programmer:
#     comp="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} & salary is {self.salary}")

class programmer(employee):
    comp="ITC Infotech"
    def showLang(self):
        print(f"The name is {self.name} and her is good at {self.language} language")

a=employee()
b=programmer()
print(a.comp,b.comp)