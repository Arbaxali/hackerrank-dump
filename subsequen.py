arr  = [1,2,3]
n = len(arr)



# for i in range(0,n):
#     # sp = i
#     # ep = i
#     # print(arr[sp:ep])
#     # if sp == ep:
#     #     ep +=1
#     #     print(arr[sp:ep])
#     sp = 0
#     ep = i+1
#     print(arr[sp:ep])
#     sp = ep
for i in arr:

    sp  = 0
    ep = i+1
    if ep < n:
        print(arr[sp:ep])
        sp = i
    elif ep == n:
        ep = 0
        sp +=1
        print(arr[sp:ep])
        ep = i+1









# even part

# res = 1
    
# for i in arr:
#     res = res * i
# print(res)    
# if res% 2 == 0:
#     print(len(arr))