# Operator Overloading 

class addition:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __add__(self):
        return self.v1 + self.v2


add = addition(5,77)

print(add.__add__())
