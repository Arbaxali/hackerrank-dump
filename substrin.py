s = "geek"
t =[]
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        t.append(s[i:j])
print(t)
        