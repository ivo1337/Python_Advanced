from collections import deque



time_neeeded = deque([int(x) for x in input().split(" ")])
tasks = deque([int(x) for x in input().split(" ")])
darth_vader = 0
thor = 0
big_blue = 0
small_yellow = 0



while time_neeeded and tasks:
    time = time_neeeded.popleft()
    task = tasks.pop()
    time_spent = task * time

    if 0 <= time_spent < 60:
        darth_vader += 1
        continue
    elif 60 <= time_spent < 120:
        thor += 1
        continue
    elif 120 <= time_spent < 180:
        big_blue += 1
        continue
    elif 180 <= time_spent < 240:
        small_yellow += 1
        continue
    elif time_spent >= 240:
        time_neeeded.append(time)
        tasks.append(task - 2)
        continue
    break

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
print(f"Darth Vader Ducky: {darth_vader}")
print(f"Thor Ducky: {thor}")
print(f"Big Blue Rubber Ducky: {big_blue}")
print(f"Small Yellow Rubber Ducky: {small_yellow}")





