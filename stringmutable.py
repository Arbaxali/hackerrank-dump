s = "abracadabra"
lst = []
lst.extend(s)
print(lst)
lst[5] = "k"
st = "".join(lst)
print(st)