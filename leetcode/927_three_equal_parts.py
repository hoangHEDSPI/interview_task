class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        numOnes = arr.count(1)
        
        # Handle corner cases
        if numOnes % 3 != 0:
            return [-1, -1]
        if numOnes == 0:
            return [0, 2]
        
        # Find the last one
        countOnes = 0
        lastValue = ""
        i = len(arr)-1
        while countOnes < numOnes // 3:
            if arr[i] == 1:
                countOnes += 1
            lastValue += str(arr[i])
            i -= 1
        lastValue = lastValue[::-1]

        # Find the first one
        j = 0
        countOnes = 0
        firstValue = ""

        # Remove non-sense zeros
        while arr[j] == 0:
            j += 1
        
        while countOnes < numOnes // 3:
            if arr[j] == 1:
                countOnes += 1
            firstValue += str(arr[j])
            j += 1

        while firstValue != lastValue and arr[j] == 0:
            firstValue += '0'
            j += 1
        if firstValue != lastValue:
            return [-1,-1]
        else:
            firstIndex = j-1
        
        # Find second value
        countOnes = 0
        secondValue = ""
        while arr[j] == 0:
            j += 1
        while countOnes < numOnes // 3:
            if arr[j] == 1:
                countOnes += 1
            secondValue += str(arr[j])
            j += 1
        while secondValue != lastValue and arr[j] == 0:
            secondValue += '0'
            j += 1
        if secondValue != lastValue:
            return [-1, -1]
        else:
            secondIndex = j
            
        return[firstIndex, secondIndex]
      
