# f = open("poems.txt","r")
# t =  f.read()
# if "Twinkle" in t:

#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")  
    
    

# f.close()



# def game():
#     return 34

# score = game()

# with open("hiscore.txt") in f:
#     hiscore = int(f.read())

# if hiscore == '' :
#     with open("hiscore.txt","w") in f:
#         f.write(str(score))   

# if hiscore < score:
#     with open("hiscore.txt","w") in f:
#         f.write(str(score))



with open("sample.txt",) as f:
    content = f.read()

content = content.replace("donkey","$$$##@^#") 
with open("sample.txt","w") as f:
    f.write(content)
      
        





