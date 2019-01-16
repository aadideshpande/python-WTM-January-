'''
Create a Temperature class. Make two methods:
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''

class temperature:
    def __init__(self,temp):
        self.temp=temp
    def convertF(self):
        return self.temp*(9/5)+32
    def convertC(self):
        return (self.temp-32)*(5/9)








n=int(input('enter 1 for celsius-->fahrenheit and 2 for fahrenheit-->celsius '))
if n==1:
    t=temperature(float(input('enter the temperature in celsius :')))
    print(t.convertF())
elif n==2:
    t = temperature(float(input('enter the temperature in fahrenheit :')))
    print(t.convertC())