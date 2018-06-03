import random 
"""
a = input()
b = input()
op = input()
if op=='add'  :
    print(a+b)
elif op=='mult' :
    print(a*b)
elif op=='div' :
    print(a/b)  
elif op=='dif' :
    print(a-b)
 """
    
x = random.randint(0,100)
y = input()
w = False
i = 0
while w==False or i>5 :
    if x==y :
        w = True
        print(w)
        print(x)
        break
    elif x<y :
        w = False
        print(w)
        print("Zahl ist kleiner")
        y = input()
        i+=1
    elif x>y :
        w = False
        print(w)
        print("Zahl ist groesser")
        y = input()
        i+=1
