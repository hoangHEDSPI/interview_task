from typing import List

if __name__ == '__main__':
    cases = int(input())
    for t in range(1, cases+1):
        N, K, P = [int(s) for s in input().split()]
        plates_piles = []
        for j in range(N):
            pile = []
            current = 0
            for s in input().split():
                current += int(s)
                pile.append(current)
            plates_piles.append(pile)
        dp = [[0 for _ in range(K)] for _ in range(N)]
        dp[0] = plates_piles[0]
        for i in range(1, N):
            for j in range(P):
                if j > i * K:
                    break
                for l in range(K):
                    if j>=l:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + plates_piles[i][j])
        ans = dp[N-1][P-1]
        print(f"Case #{t}: {ans}")
    