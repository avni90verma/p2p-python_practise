'''def fact(n):
    if n==0:
      ans=1
    else:
        ans=n*fact(n-1)
    return ans 

 
print(fact(5))    '''


# Anonymous function
# a function without a name 
'''keyword lamda is used
lamba input:expression'''

'''s=lambda n:n*n
print(s(6))'''

# Positional arguments
def calc(a,b):
    sum=a+b
    sub=a-b
    multi=a*b
    div=a/b
    return (sum,sub,multi,div)    

r=calc(100,50)   #this r will be treated as tuple
# a is reserved for 100 and b is reserved for 50.

print(type(r))

for i in r:
    print(i)


#alternate method below

'''x,y,z,w=calc(a=100,b=50)
x,y,z,w=calc(b=100,a=50)
print(x)
print(y)
print(z)
print(w)'''







#KEYWORD ARGUMENT
def calc(a,b):
    sum=a+b
    sub=a-b
    multi=a*b
    div=a/b
    return (sum,sub,multi,div)    


'''x,y,z,w=calc(a=100,50)
#x,y,z,w=calc(100,a=50)# this is wrong
print(x)
print(y)
print(z)
print(w)'''    


#Var agrument

def sum(*n): # star refers it can store any number of argumnets
    sum=0
     for x in n:
        sum=sum+x
    print('sum is :',result) 

sum(9)


