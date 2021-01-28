class Heap:
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    def buildMaxHeap(self, arr, n):
        for i in range(n/2, -1, -1):
            self.heapify(arr, n, i) 

arr = [1,4,2,6,7,3,5,3,2,7,4]
h = Heap()
h.buildMaxHeap(arr,len(arr))
print(arr)