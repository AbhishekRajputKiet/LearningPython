class employee :
   def __init__(self):
      # name function cannot be change in other funtion or class
      # name function is procted 
      self.__name="Abhishek Rajput"
      # bit _name can be access directly 
a=employee()
# print(a.__name) can not be acces directly 
print(a._employee__name)

