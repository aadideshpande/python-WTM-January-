
file=open('stud_details.rtf','w')
list1=[]
n=int(input('enter number of students : '))






for i in range(n):
    file.write('\n ')

    file.write(input('enter student name  : '))
    file.write(' \n maths ' )
    file.write(input('enter maths marks  : '))
    file.write(' \n ')

    file.write(' \n physics ')
    file.write(input('enter physics marks  : '))
    file.write(' \n ')

    file.write(' \n chemistry ')
    file.write(input('enter chemistry marks  : '))
    file.write(' \n ')

file.close()