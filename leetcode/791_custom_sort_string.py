class Solution:    
    def customSortString(self, order: str, str: str) -> str:
        orderDict = {key: value for value, key in enumerate(order)}
        
        for c in str:
            if not c in orderDict:
                orderDict[c] = float('inf')
        
        return ''.join((sorted(str, key=lambda x: orderDict[x])))
