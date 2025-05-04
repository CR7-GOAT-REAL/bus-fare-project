class Bus:
    def __init__(self, num_seats, fare_passenger):
        self.num_seats = num_seats
        self.fare_passenger = fare_passenger

    def total_fare(self):
        return self.num_seats * self.fare_passenger

bus = Bus(30, 1)
print(bus.total_fare())