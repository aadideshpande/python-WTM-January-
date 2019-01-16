
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def setage(self):
        self.age = int(input('enter student age : '))
    def setmarks(self):
        self.marks = int(input('enter student marks : '))

    def display(self):
        print('name :    ',s1.name)
        print('roll no : ',s1.rollno)
        print('age:      ',s1.age)
        print('marks :   ',s1.marks)




s1=student('aadi',59)
s1.setage()
s1.setmarks()
s1.display()

