class Employee:
    company = 'Google'
    def showclass(self):
        print('it an employee')
    
class programmer(Employee):
    langauge = 'python'
    #company = 'youtube'  # overriding 
    def getlangauge(self):
        print(f"the lang is {self.langauge}")
    def showclass(self):
        print('this is an employee class') 
        
        
p = programmer()
p.showclass()
# p = programmer()
# print(p.company) #overriding
p.getlangauge()