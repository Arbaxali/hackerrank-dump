s = "HelloWOrld"
sr = ""


for i in range(0,len(s)):
    if s[i].isupper():
        sr += s[i].lower()
    else:
        sr += s[i].upper()


print(sr)       
    
        


# for i in s:
#     if i.isupper:
#         print(i)
#     else:
#         print("s",i)    