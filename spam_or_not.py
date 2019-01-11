#Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam=input('enter 1 or 2 :  ')

if int(spam)==1:
    print('hello')
elif int(spam)==2:
    print('howdy')
else:
    print('greetings!')