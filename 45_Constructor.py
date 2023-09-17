class person :
    # name = "Abhishek Rajput"
    # occ = "Mechain learning"
    # __init__ use to initiasilize the constructor
    def __init__(self,name,occ):
        print("Hy im a person")
        self.name=name
        self.occ=occ

    def info(self):
        print(f"My name is {self.name} and occ is {self.occ}")

s=person("Abhishek Rajput","Mechain learning")
m=person("Rajput","learning")
s.info()
m.info()