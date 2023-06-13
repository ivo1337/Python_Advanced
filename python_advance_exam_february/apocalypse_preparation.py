from collections import  deque


textiles = deque([int(x) for x in input().split(" ")])
healing_kits = deque([int(x) for x in input().split(" ")])

# Patch	30
# Bandage	40
# MedKit	100
patch = 0
bandage = 0
med_kit = 0



while textiles and healing_kits:
    textile = textiles.popleft()
    healing_kit = healing_kits.pop()

    combined = textile + healing_kit

    if combined == 30:
        patch += 1
        continue
    elif combined == 40:
        bandage += 1
        continue
    elif combined == 100:
        med_kit += 1
        continue
    elif combined > 100:
        med_kit += 1
        remaining = combined - 100
        reaming = healing_kits.pop()
        remaining += reaming
        healing_kits.append(remaining)
        continue
    else:
        additional = healing_kit + 10
        healing_kits.append(additional)
        continue
    break

if len(textiles) == 0 and len(healing_kits) == 0:
    print("Textiles and medicaments are both empty.")

elif len(textiles) == 0:
    print("Textiles are empty.")

elif len(healing_kits) == 0:
    print("Medicaments are empty.")

items = [("Patch", patch), ("Bandage", bandage), ("MedKit", med_kit)]
items.sort(key=lambda x: (-x[1], x[0]))

for item_name, item_count in items:
    if item_count > 0:
        print(f"{item_name} - {item_count}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
