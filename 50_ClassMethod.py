class Employee :
    company="TCS"
    def show(self):
        print(f"Name of company is {self.company} and my name is {self.name}")
    @classmethod
    # class decorater is use to pass the first element of function as a class 
    def changecomp(cls,newcompany):
        cls.company=newcompany
e1=Employee()
e1.name="Abhishek Rajput"
e1.show()
e1.changecomp("Apple")
e1.show()
print(Employee.company) 