def greatest(a,b,c):
    if(a>b and a>c):
        print("greatest number= ",a)
    elif(b>a and b>c):
        print("greatest number= ",b)
    else:
        print("greatest number= ",c)    

greatest(10,20,3)        


def convert(a):
    c = (a * 9/5) + 32 
    print(f"celsius to Fahrenheit=", c)

convert(70)


def sum(n):
    if n==1 :
        return 1
    else:
        return n+ sum(n-1)

print(sum (3))        


n=3
for i in range (n,0,-1):
    for j in range(i):
        print("*",end="")
    print()


def conversion(a):
    cms= a* 2.54
    print("inches to centimeter=" , cms)


conversion(5)    


def replace( string, word):
    newstring = string.replace(word," ")
    return newstring.strip()

this = "    this is avni"
n=replace(this, "avni")
print(n)
