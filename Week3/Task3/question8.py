"""show class method, static method and instance method with simple example. 
"""
class Sample:

    # Instance Method
    def method_instance(self):
        print("Instance method called")

    # Class Method
    @classmethod
    def method_class(cls):
        print("Class method called")

    # Static Method
    @staticmethod
    def method_static():
        print("Static method called")

obj = Sample()

obj.method_instance()
Sample.method_class()
Sample.method_static()
