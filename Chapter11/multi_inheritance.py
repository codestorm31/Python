class employee:
    comp="ITC"
    name="Default"
    def show(self):
        print(f"The name is {self.name} & Company is {self.comp}")
        
class coder:
    lang="Python"
    def printLang(self):
        print(f"Out of all the languages here is : {self.lang}")
    
class programmer(employee,coder):
    comp="ITC Infotech"
    def showLang(self):
        print(f"The name is {self.name} and her is good at {self.language} language")

a=employee()
b=programmer()
a.show()