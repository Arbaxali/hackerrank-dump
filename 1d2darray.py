## converting 1d array to 2d array


import math
lst = lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
lst1 = []

lenn = len(lst)
n = math.sqrt(lenn)
n = int(n)
for i in range(0, lenn+1,n):
    fianl = lst[i:i+n]
    if len(fianl) == n:
        lst1.append(fianl)

print(lst1)  
