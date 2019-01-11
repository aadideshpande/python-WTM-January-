#required argument

def hello(x):
    print('hello ')

x=90
hello(x)

#keyword argument

def welcome(a):
    print(a)

welcome(a=45)

# default argument

def sum(num1,num2=2):
    sum_1=num2+num1
    print(sum_1)

sum(3)

# variable length argument

def new(x,*y):
    print(x)

    for i in y:
        print(i)
    return

new(10,32,55)
