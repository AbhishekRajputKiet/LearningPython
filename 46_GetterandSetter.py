
class Myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"Value is {self._value}")
    
    @property
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter 
    def ten_value(self,newval):
        self._value=newval/10
    
obj=Myclass(10)
obj.ten_value=55
print(obj.ten_value)
obj.show()