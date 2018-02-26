def climbingStairs(n):
    if n == 1: return 1
    elif n == 2: return 2
    else:
        S = [0 for i in range(n)]
        S[0] = 1
        S[1] = 2
        for i in range(2, n):
            S[i] = S[i-1] + S[i-2]
        
        return S[n-1]

    
print climbingStairs(17)