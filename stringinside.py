s = "hello world how are you"

s = s.split(" ")
lst = []
for i in range(0, len(s)):
    lst.extend(s[i])

print(lst)