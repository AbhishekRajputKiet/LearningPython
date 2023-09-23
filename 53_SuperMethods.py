# Super method :- this use to call chile class method to parant class method
class parant:
    def parant_method(self):
        print("This the Parant function")
class child(parant):
    # def parant_method(self):
    #     print("Abhishek Rajput")
    #     super().parant_method()
    def child_method(parant_method):
        print("This child function")
        super().parant_method()

child_objact=child()
child_objact.child_method()
child_objact.parant_method()




