# max_flights problem self implemented solution, probably not efficient enough...
class Flight:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Flight[start: {self.start}, end: {self.end}]"


def max_flight(flights):
    if type(flights) != list:
        return "Please provide list arguments!"
    if len(flights) == 0:
        return 0

    min_start = flights[0].start
    max_end = flights[0].end
    for flight in flights:
        if flight.start <= min_start:
            min_start = flight.start
        if flight.end >= max_end:
            max_end = flight.end

    max_flights = []
    for i in range(min_start, max_end + 1):
        flight_count = 0
        for flight in flights:
            if flight.start <= i and i <= flight.end:
                flight_count += 1
        max_flights.append(flight_count)
    print(max_flights)
    return max(max_flights)


if __name__ == "__main__":
    flights = [
        Flight(4, 8),
        Flight(2, 5),
        Flight(17, 20),
        Flight(10, 21),
        Flight(9, 18),
    ]

    print(max_flight(flights))

    print(max_flight("flights"))  # invalid
