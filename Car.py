from Ride import Ride

class Car:

    def __init__(self):
        self._rides = []
        self._time_finished = 0
    
    @property
    def rides(self):
        return self._rides

    @property
    def time_finished(self):
        return self._time_finished

    @property
    def last_position(self):
        if len(self._rides) == 0:
            return (0, 0)
        return self._rides[-1].end

    def when_can_ride_start(self, ride):
        return max(self._time_finished + Ride.distance_between(self.last_position, ride.start), ride.earliest_start)

    def add_ride(self, ride):
        self._time_finished = self.when_can_ride_start(ride) + ride.distance
        self._rides.append(ride) 

    def can_take_ride(self, ride, steps):
        if len(self._rides) == 0:
            return True

        total_time = self.when_can_ride_start(ride) + ride.distance
        return total_time <= steps and total_time <= ride.finish_time

    def __str__(self):
        # Add the number of rides to the front of the list        
        self._rides.insert(0, len(self._rides))
        
        # [a, b, c, d] => a b c d
        return str(self._rides).translate({ord(i): None for i in '[],'})

    def __repr__(self):
        return self.__str__()