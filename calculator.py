print('='*60)
print('             CALCULATOR')
print('='*60)
x=float(input('enter one number :'))
y=float(input('enter another number:'))
print('1.addition')
print('2.subraction')
print('3.multiplication')
print('4.division')
choice=input('choose any one operator 1/2/3/4 :')
if choice =='1':
    print('result :' ,x+y)
elif choice =='2':
     print('result:' ,x-y)
elif choice=='3':
      print('result :' ,x*y)
elif choice=='4':
      print('result:' ,x/y)
else:
       print('invalid choice')