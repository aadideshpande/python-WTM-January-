n=int(input('enter number between 1 to 7 , '))

dict={}
dict[1]='sunday'
dict[2]='monday'
dict[3]='tuesday'
dict[4]='wednesday'
dict[5]='thursday'
dict[6]='friday'
dict[7]='saturday'


def day(n):



            if  n>7 or n<1 :
                print(' not allowed, enter between 1 to 7 ')
            else:
                print(dict[n])






day(n)