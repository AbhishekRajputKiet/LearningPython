# Self paramater is a reference to the current instance of the class ,
# it use to access the variable that belongs to the class

class person:
    name = "Abhishek Rajput"
    occupication = "B.tech"
    netWerth=10
    def info(self):
        print(f"My name is {self.name} and I am doing {self.occupication}")
    
a=person()
print(a.name , a.netWerth,a.occupication)
a.name="vikash"
a.netWerth=15
print(a.name , a.netWerth,a.occupication)
a.info()
