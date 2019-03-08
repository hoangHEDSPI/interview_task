def firstDuplicate(a):
    b = []
    for i in range(len(a)+1):
        b.append(0)
    for i in range(len(a)):
        b[a[i]] += 1
        if b[a[i]] > 1:
            return a[i]
    return -1
        
