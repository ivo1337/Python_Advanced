import time
start = time.time()
list_queue = [el for el in range(1, 1000000)]

while list_queue:
    list_queue.pop(0)
    print(list_queue)

diff = time.time() - start
print(diff)