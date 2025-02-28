from collections import Counter 
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    
    heap = [(-freq, num) for num, freq in count.items()]

    top_k = []

    for _ in range(k):
        freq, num = heapq.heappop(heap)
        top_k.append(num)

    return top_k

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(topKFrequent([1], 1))  # [1]
print(topKFrequent([1, 2], 2))  # [1, 2]