# Base class
class Grandfather:
    def show(self):
        print("This is the Grandfather class.")

# Derived class (inherits from Grandfather)
class Father(Grandfather):
    def show(self):
        print("This is the Father class.")

# Derived class (inherits from Father)
class Son(Father):
    def show(self):
        print("This is the Son class.")

# Create object of Son class
obj = Son()

# Calling show() methods
obj.show()              # Calls Son's show()
Father.show(obj)       # Calls Father's show()
Grandfather.show(obj)  # Calls Grandfather's show()
