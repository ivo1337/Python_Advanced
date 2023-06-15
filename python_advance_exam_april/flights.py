def flights(*args):
    flight_data = {}
    destination = None

    for arg in args:
        if arg == "Finish":
            break

        if destination is None:
            destination = arg
        else:
            passengers = int(arg)
            if destination in flight_data:
                flight_data[destination] += passengers
            else:
                flight_data[destination] = passengers
            destination = None

    return flight_data


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))