def timeConversion(s):
    # Write your code here

    l = list(s)


    ss = s[-2:]
    hh = int(s[:2])

    if ss == "PM" and hh < 12:
        hh = 12 + hh
        hh = str(hh)
        l[:2] = hh
        s1 ="".join(l)
        s2 = s1[:8]

    elif ss== "AM" and hh == 12:
        l[0] = "0"
        l[1] = "0"
        s1 ="".join(l)
        s2 =s1[:8]
    elif ss == "AM":
        s2 = s[:8]
    
    elif ss == "PM" and  hh == 12:
        s2 = s[:8]

    return s2
