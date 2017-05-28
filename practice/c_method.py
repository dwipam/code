class employee(object):
    x=""
    def __init__(self,name):
        self.name = name
    @classmethod
    def from_e(cls,name):
        name = name
        return cls(name)
    @classmethod
    def set_e(name):
       self.x = name

e1 = employee.from_e('str')
e21 = employee.from_e('str2')
e1.set_e("new")

print(e21.x)
