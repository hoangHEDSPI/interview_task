from typing import List

def solve(n: int, budget: int, prices: List[int]):
    prices.sort()
    ans = 0
    consumed_cost = 0
    while consumed_cost <= budget and ans < len(prices):
        consumed_cost += prices[ans]
        if consumed_cost <= budget:
            ans += 1
        else:
            break
    return ans

if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        houses_and_budget = [int(k) for k in input().split()]
        prices = [int(k) for k in input().split()]
        print(f"Case #{i+1}: {solve(houses_and_budget[0], houses_and_budget[1], prices)}")
    