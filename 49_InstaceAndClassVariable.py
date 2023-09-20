
class Employee:
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.03
    def show(self):
        print(f"Name of imployee is {self.name} and {self.raise_amount}")
a=Employee("abhishek")
a.show()
a.raise_amount=0.05
a.show()
Employee.show(a)