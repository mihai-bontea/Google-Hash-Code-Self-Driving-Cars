from Ride import Ride
from Car import Car

class Data:
    def __init__(self, filename):
        with open(filename, 'r') as fin:
            first_line = fin.readline()
            info = first_line.strip().split(' ')

            # Read the general information
            self._rows = int(info[0])
            self._columns = int(info[1])
            self._nr_vehicles = int(info[2])
            self._nr_rides = int(info[3])
            self._bonus = int(info[4])
            self._nr_steps = int(info[5])

            # Read the rides
            self._rides = []
            for i in range(self._nr_rides):
                current_line = fin.readline()
                ride_data = current_line.strip().split(' ')

                # Read the coordinates of the start and end of ride
                start_x = int(ride_data[0])
                start_y = int(ride_data[1])

                end_x = int(ride_data[2])
                end_y = int(ride_data[3])

                # Read the earliest start and finish time
                early = int(ride_data[4])
                finish = int(ride_data[5])

                # Add to list if data is valid
                if Ride.is_valid((start_x, start_y), (end_x, end_y), early, finish):
                    ride = Ride((start_x, start_y), (end_x, end_y), early, finish, i)
                    self._rides.append(ride)
    
        # Initialize a list containing the given amount of cars
        self._cars = []
        for _ in range(self._nr_vehicles):
            self._cars.append(Car())
    
    def write_to_file(self, filename):
        with open(filename, 'w') as fout:
            for car in self._cars:
                fout.write(str(car) + '\n')

    """Getters"""

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def nr_vehicles(self):
        return self._nr_vehicles

    @property
    def nr_rides(self):
        return self._nr_rides

    @property
    def bonus(self):
        return self._bonus

    @property
    def nr_steps(self):
        return self._nr_steps

    @property
    def cars(self):
        return self._cars

    @property
    def rides(self):
        return self._rides

    """Setters"""

    @rows.setter
    def rows(self, value):
        self._rows = value

    @columns.setter
    def columns(self, value):
        self._columns = value

    @nr_vehicles.setter
    def nr_vehicles(self, value):
        self._nr_vehicles = value

    @nr_rides.setter
    def nr_rides(self, value):
        self._nr_rides = value

    @bonus.setter
    def bonus(self, value):
        self._bonus = value

    @nr_steps.setter
    def nr_steps(self, value):
        self._nr_steps = value

    @cars.setter
    def cars(self, value):
        self._cars = value

    @rides.setter
    def rides(self, value):
        self._rides = value