print("square root of following")
print("formula = [-b+root of (b^2-4ac)]/2a","[-b-root of (b^2-4ac)]/2a")
print("equation format-------> X^2 + 2X + 6 OR  X^2 - 2X - 6")
b=int(input("enter a value of b"))
a=int(input("enter a value of a"))
c=int(input("enter a value of c"))
bb=b**2
print("value of b^2---->",bb)
cc=4*a*c
print("value of 4ac---->",cc)
dd=2*a
print("value of 2a---->",dd)
r=bb-cc
if(r<0):
    print("THE ROOTS ARE IMAGINERY AND ARE COMPLEX ROOTS")
    r=r*(-1)
    l=("√",r,"i")
    print("root 1----> [-",b,"+","√",r,"i]/",2*a)
    print("root 2----> [-",b,"-","√",r,"i]/",2*a)
elif(r>0):
    print("THE ROOTS ARE REAL")
    u=(r**0.5)
    print("root1----> [-",b,"+",u,"]/",2*a)
    print("root2----> [-",b,"-",u,"]/",2*a)
    
    
