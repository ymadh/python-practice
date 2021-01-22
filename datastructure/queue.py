from collections import deque

# queues are less performant
# queue = [1, 2, 3]

# dequeue object helps performance
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")