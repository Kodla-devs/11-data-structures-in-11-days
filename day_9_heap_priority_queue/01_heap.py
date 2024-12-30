import heapq

li = [5, 7, 9, 2, 3]

heapq.heapify(li)

print(li)

neg_li = [-x for x in li]
heapq.heapify(neg_li)
max_heap = [-x for x in neg_li]

print(max_heap)

heapq.heappush(li, 4)
print(li)

heapq.heappop(li)
print(li)

heapq.heappushpop(li, 10)
print(li)

print(heapq.nlargest(2, li))

print(heapq.nsmallest(2, li))

for _ in range(len(li)):
    print(heapq.heappop(li))