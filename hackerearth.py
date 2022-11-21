def Cyber_Security (L,R):
    c=0
    for i in range(L,R+1):
        i=str(i)
        if i[0]==i[-1]:
            c+=1
    

    return c

print(Cyber_Security(13566,450999))