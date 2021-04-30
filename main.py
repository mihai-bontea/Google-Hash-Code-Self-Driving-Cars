from Data import Data
from Ride import Ride
from math import inf

in_files = ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]

for file in in_files:
    print("Now working on file", file)

    # Reading the data
    data = Data("./Input/" + file)

    for car in data.cars:
        can_take_more_rides = True

        while can_take_more_rides:
            can_take_more_rides = False
            soonest_start = inf
            soonest_start_bonus = inf

            best_ride_bonus = None
            best_ride_without = None

            for ride in data.rides:
                if car.can_take_ride(ride, data.nr_steps):
                    can_take_more_rides = True
                    
                    if Ride.can_start_on_time(ride, car):
                        if car.when_can_ride_start(ride) <= soonest_start_bonus:
                            soonest_start_bonus = car.when_can_ride_start(ride)
                            best_ride_bonus = ride
                    else:
                        if car.when_can_ride_start(ride) <= soonest_start:
                            soonest_start = car.when_can_ride_start(ride)
                            best_ride_without = ride
            
            chosen_ride = None
            if best_ride_bonus != None and best_ride_without != None:
                chosen_ride = best_ride_bonus if (soonest_start_bonus - data.bonus <= soonest_start) else best_ride_without

            elif best_ride_bonus != None:
                chosen_ride = best_ride_bonus
            elif best_ride_without != None:
                chosen_ride = best_ride_without

            if chosen_ride != None:
                car.add_ride(chosen_ride)
                data.rides.remove(chosen_ride)

    out_filename = "./Output/" + (file.split('.'))[0] + ".out"
    data.write_to_file(out_filename)
