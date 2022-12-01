a=float(input("Enter value of first interval"))
b=float(input("Enter value of second interval"))
e=float(input("Enter value of zero"))

def f(x):
    return(x**2-x-1)

def regulafalsi(a,b):
    
    if(f(a)*f(b)>0):
        print("invalid interval")
    else:
     m=(a*f(b)-b*f(a))/(f(b)-f(a))
     i=1
     while(abs(f(m))>e):
         print(i," ",a," ",b," ",m," ",f(m),"  ",(f(a)*f(m)))
         if(f(m)<0):
             a=m
         else:
             b=m
         m=(a*f(b)-b*f(a))/(f(b)-f(a))
         i=i+1
         print(i," ",a," ",b," ",m," ",f(m),"  ",(f(a)*f(m)))
regulafalsi(a,b)
                     



