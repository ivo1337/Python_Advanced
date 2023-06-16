from collections import deque

presents = deque([int(x) for x in input().split()])
gift_magic= deque([int(x) for x in input().split()])

gemstone = 0
porcelain = 0
gold = 0
diamond = 0

while presents and gift_magic:
    present = presents.pop()
    magic = gift_magic.popleft()

    gift = present + magic

    if 100 <= gift <= 199:
        gemstone += 1

    elif 200 <= gift <= 299:
        porcelain += 1

    elif 300 <= gift <= 399:
        gold += 1

    elif 400 <= gift <= 499:
        diamond += 1

    elif gift < 100:
        if gift % 2 == 0:
            present_new = present * 2
            magic_new = magic * 3

            gift = present_new + magic_new

            if 100 <= gift <= 199:
                gemstone += 1

            elif 200 <= gift <= 299:
                porcelain += 1

            elif 300 <= gift <= 399:
                gold += 1

            elif 400 <= gift <= 499:
                diamond += 1

        elif gift % 2 != 0:

            gift_new = gift * 2

            if 100 <= gift_new <= 199:
                gemstone += 1

            elif 200 <= gift_new <= 299:
                porcelain += 1

            elif 300 <= gift_new <= 399:
                gold += 1

            elif 400 <= gift_new <= 499:
                diamond += 1

    elif gift > 499:
        gift_new = gift / 2
        if 100 <= gift_new <= 199:
            gemstone += 1

        elif 200 <= gift_new <= 299:
            porcelain += 1

        elif 300 <= gift_new <= 399:
            gold += 1

        elif 400 <= gift_new <= 499:
            diamond += 1


if (gemstone > 0 and porcelain > 0) or (gold > 0 and diamond > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if presents:
    print(f"Materials left: {', '.join([str(x) for x in presents])}")
if gift_magic:
    print(f"Magic left: {', '.join([str(x) for x in gift_magic])}")

items = [("Gemstone", gemstone), ("Porcelain Sculpture", porcelain), ("Gold", gold), ("Diamond Jewellery", diamond)]
items.sort()

for item_name, item_count in items:
    if item_count > 0:
        print(f"{item_name}: {item_count}")