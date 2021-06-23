b= set()
print(type(b))

#Adding values to an empty set

b.add(5)
b.add(6)
b.add(7)
b.add(8)
b.add((2,4,5))

# b.add[2,4,5]  #We cannot add list in a set beacuse list is changeable

# b.add(2,4,5) #we can add tuple in list beacause it is non changeable like sets

print(len(b))
b.remove(5)
b.pop()   #kuch bhi remove kr dega set mae se

b.union({12,11})

print(b)