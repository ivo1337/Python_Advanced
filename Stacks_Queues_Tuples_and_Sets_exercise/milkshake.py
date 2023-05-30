from collections import deque


chocolate = deque(int(x) for x in input().split(", "))
milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolate and milk:
    chocolates = chocolate.pop()
    cup_milk = milk.popleft()

    if chocolates <= 0 and cup_milk <= 0:
        continue
    elif chocolates <= 0:
        milk.appendleft(cup_milk)
        continue
    elif cup_milk <= 0:
        chocolate.append(chocolates)
        continue

    if chocolates == cup_milk:
        milkshakes += 1
    else:
        milk.append(cup_milk)
        chocolate.append(chocolates - 5)
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolate) or 'empty'} ")
print(f"Milk: {', '.join(str(x) for x in milk) or 'empty'} ")