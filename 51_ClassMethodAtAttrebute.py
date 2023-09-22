
class Employee :
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstring(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

    
a=Employee("Abhishek",50000)
print(a.name,a.salary)

string="Abhishek-12000"
b=Employee.fromstring(string)
print(b.name,b.salary)
class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromstring(cls,string):
        name,age=string.split(',')
        return cls(name,int(age))
c=Person.fromstring("abhishek , 21")
print(c.name , c.age)
        



