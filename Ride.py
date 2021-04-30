
class Ride:
    def __init__(self, start, end, earliest_start, finish_time, ID):
        self._start = start
        self._end = end
        self._earliest_start = earliest_start
        self._finish_time = finish_time
        self._ID = ID

    @property
    def ID(self):
        return self._ID
    
    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def earliest_start(self):
        return self._earliest_start

    @property
    def finish_time(self):
        return self._finish_time
    
    @property
    def distance(self):
        return self.distance_between(self._start, self._end)

    @staticmethod
    def distance_between(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    @staticmethod
    def is_valid(start, end, earliest_start, finish_time):
        dist = Ride.distance_between(start, end)
        return dist <= (finish_time - earliest_start)

    @staticmethod
    def can_start_on_time(ride, car):
        return car.time_finished + Ride.distance_between(car.last_position, ride.start) <= ride.earliest_start

    @staticmethod
    def can_finish_early(ride, car):
        finish = car.when_can_ride_start(ride) + ride.distance
        return finish <= ride.finish_time

    def __str__(self):
        return str(self._ID)

    def __repr__(self):
        return self.__str__()