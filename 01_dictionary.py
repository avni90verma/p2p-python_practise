mydict={
    "Fast": "In a quick manner",
    "Harry": "a coder",
    "MARKS":[2,3,5],
    "anotherdict": {'Avni':'a student',
    'sachin':'a player'},
     1: 2
}
'''print(mydict['Fast'])
print(mydict['Harry'])
print(mydict['anotherdict']['Avni'])

mydict['MARKS']=[45,68,72]
print(mydict['MARKS'])    #it is mutable'''

# dictionary methods 

print(list(mydict.keys()))   #prints the dictionary in the form of list
print(mydict.values())      #prints the keys of dictionary
print(mydict.items())  #prints the (keys and values)of all the contents 

updatedict={                # UPDATING A DICTIONARY
    "Lovish": "Friend"
}
mydict.update(updatedict)
print(mydict)

print(mydict.get("harry2"))  #it returns None
print(mydict["harry2"]))    #it throws eroor









