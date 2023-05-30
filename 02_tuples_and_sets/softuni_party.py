number_of_guests = int(input())

reservation = {input() for _ in range(number_of_guests)}
guests_who_came = input()

while guests_who_came != "END":
    reservation.remove(guests_who_came)
    guests_who_came = input()

print(len(reservation))
print("\n".join(sorted(reservation)))












