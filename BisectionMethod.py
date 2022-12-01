a=float(input("Enter value of first interval"))
b=float(input("Enter the value of second interval"))
e=float(input("Enter the place fo error"))

def f(x):
    return (x**2-x-1)

def bisection(a,b):

    if(f(a)*f(b)>0):
        print("invalid interval")
    else:
     m=(a+b)/2
     i=1
     while(abs(f(m))>e):
         print(i," ",a," ",b," ",m," ",f(m),"  ",(f(a)*f(m)))
         if((f(a)*f(m)>0)):
             a=m
         else:
             b=m
         m=(a+b)/2
         i=i+1
         print(i," ",a," ",b," ",m," ",f(m),"  ",(f(a)*f(m)))
bisection(a,b)
                     
         
         