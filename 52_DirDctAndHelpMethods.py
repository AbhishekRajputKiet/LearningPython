class person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.roll=7
x=person("Abhishek",20)
print(x.__dict__)
    


x=[1,2,3]
print(dir(x))
print(x.__add__)
print(x)