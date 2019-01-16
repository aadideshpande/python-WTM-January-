class myClass:
    x=5 # x is a property of the class

p1=myClass()    # p1 is an object
print(p1.x)


class person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age


p1=person('aadi',18)

print(p1.name)
print(p1.age)