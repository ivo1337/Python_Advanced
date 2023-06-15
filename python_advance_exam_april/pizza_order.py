from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
total_pizzas = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    current_employee = employees.pop()

    if current_order <= 0:
        employees.append(current_employee)
        continue
    elif current_order > 10:
        employees.append(current_employee)
        continue
    elif current_order <= 10:
        if current_order <= current_employee:
            total_pizzas += current_order
        elif current_order > current_employee:
            total_pizzas += current_employee
            pizza_orders.appendleft(current_order - current_employee)
        continue
    elif current_order > current_employee:
        total_pizzas += current_employee
        pizza_orders.appendleft(current_order - current_employee)

    break

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")