from collections import deque

q = deque()

queue = deque(["kodla", 1, 5.1, True])

queue.append(3)
print(queue)

queue.pop()
print(queue)

print(not queue)

print(queue.count("kodla"))

print(len(queue))