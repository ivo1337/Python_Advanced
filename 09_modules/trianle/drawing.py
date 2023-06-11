def draw_upper(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=" " )
        print()

def draw_down(n):
    for row in range(n - 1, 0, -1):
        for num in range(1, row+1):
            print(num, end=" ")
        print()


def draw_triangle(n):
    draw_upper(n)
    draw_down(n)
