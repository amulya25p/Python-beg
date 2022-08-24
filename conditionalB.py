#conditional operators, try and except statement
#h=int(input('enter the hours'))
#r=int(input('enter the rate'))

#if h>40:
 #   print('pay=', (40*10)+(h-40)*15)
#else:
 #   print('pay=',h*10)

r=input('enter the rate')
h=input('enter the hours')
try:
    if type(h) != int or type(r) != int:
        print('enter numeric value')
except:
 if h>40:
    print('pay=', (40*10)+(h-40)*15)
 else:
    print('pay=',h*10)


