from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()

    challenge = tool * substance

    if challenge in challenges:
        challenges.remove(challenge)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance == 0:
            continue
        else:
            substances.append(substance)

if not substances and challenges:
    if challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
