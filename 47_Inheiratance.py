# // programmer contain the properties of employee also 
class employee :
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"Name of user is {self.name} and id is {self.id}")
class programmer(employee):
    def showlanguage(self):
        print(f"Defoult language is python ")


obj=employee("Abhi rajput",420)
obj.show()
obj2=programmer("yadav",320)
obj2.showlanguage()
obj2.show()