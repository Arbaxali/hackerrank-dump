s = "abcdcdccdc"
ss = "cdc"
l = len(ss)
cou  = 0

for i in range(0, len(s)):
    if ss == s[i:i+l]:
        print(s[i:i+l])

  
