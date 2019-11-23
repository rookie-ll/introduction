import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

big=heapq.nlargest(3,nums)
small=heapq.nsmallest(3,nums)
print(big)
print(small)