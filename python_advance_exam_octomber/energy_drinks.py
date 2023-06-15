from collections import deque

caffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])
caffeine_for_the_night = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    caffeine_total = current_caffeine * current_energy_drink

    if caffeine_total <= 300:
        if caffeine_for_the_night + caffeine_total >= 300:
            energy_drinks.append(current_energy_drink)
            caffeine_for_the_night -= 30
            continue
        else:
            caffeine_for_the_night += caffeine_total
            continue
    else:
        energy_drinks.append(current_energy_drink)
        if caffeine_for_the_night <= 0:
            continue
        else:
            caffeine_for_the_night -= 30
            continue

    break

if energy_drinks:
    print("Drinks left: " + ", ".join([str(x) for x in energy_drinks]))

if not energy_drinks:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_for_the_night} mg caffeine.")