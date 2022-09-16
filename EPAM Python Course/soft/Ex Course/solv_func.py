def ask_value():
    global a,b,c
    print("Hi,user! Enter your arguments A")
    a=int(input())
    print("And argument B")
    b=int(input())
    print("So we need argument C")
    c=int(input())
    return a,b,c
    

def discriminant(a,b,c):
    d =b**2-4*a*c
    print("Diskriminant = ")
    print(d)
    return d

def roots(a,b,c,d):
    if d > 0:
     print("We have 2 roots")
     x1= (-b-d**0.5)/(2*a)
     x2= (-b+d**0.5)/(2*a)
     print (x1,x2)
      
    if d == 0:
     print("We have 1 root")
     x3=-b/(2*a)
     print (x3)
    if d < 0:
     print("We have no roots")

def solv_square():
    ask_value()
    d = discriminant(a,b,c)
    roots(a,b,c,d)