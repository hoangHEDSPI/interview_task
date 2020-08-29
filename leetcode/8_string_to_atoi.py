def myAtoi(str: str) -> int:
    maxINT = 2**31-1
    minINT = -2**31
    str = str.strip()
    if len(str) == 0 or (str[0] != "-" and str[0] != "+" and str[0].isdigit() == False) or (len(str) == 1 and str[0] == "-") or (len(str) == 1 and str[0] == "+"):
        return 0
    num = ""
    for i, x in enumerate(str):
        if x == "." and i == 0:
            pass
        if (x== "+" or x == "-") and i == 0:
            num += x
        if not x.isdigit() and i != 0:
            num += "."
        else:
            num += x
    print(num)
    num = num.split(".")
    print(num[0])
    if len(num[0]) == 1 and num[0][0].isdigit() == False:
        return 0
    if len(num[0]) >= 3 and (num[0][0:2] in ("+-", "-+")):
        return 0
    return max(minINT, min(int(num[0]), maxINT))    
        
        

print(myAtoi("   -42"))