class MyClass:
    def method(self):
        return "instance method"
    
    @classmethod
    def classmethod(cls):
        return "class method"
    
    @staticmethod
    def staticmethod():
        return "static method"
    

my_class=MyClass()
print(my_class.method())
print(my_class.classmethod())
print(my_class.staticmethod())