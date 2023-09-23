class Employee :
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name,id,roll):
        # self.name=name
        # self.id=id
        super().__init__(name,id)
        self.roll=roll
x=Employee("Vikash",420)
y=Programmer("Abhishek",1180,7)
print(y.name)
print(y.roll)
print(y.id)