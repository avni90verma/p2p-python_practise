for i in range(1,21):
    with open("tables\multiplication_table_of_{2}","w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j} = {i*j} \n" )
    break

    
