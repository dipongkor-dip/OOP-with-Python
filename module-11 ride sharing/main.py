from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Bike, Car

ride_sharing = RideSharing("XYZ company")

driver1 = Driver("driver1", "ali@gmail.com", 2345, "Rajshai")
ride_sharing.add_driver(driver1)

rider1 = Rider("Rider1", "raider1@gmail.com", 4272, "Dhaka", 1200)
ride_sharing.add_rider(rider1)

rider1.request_ride(ride_sharing, "Uttra", "car")


driver1.reach_destination(rider1.current_ride)

rider1.show_current_ride()

print(ride_sharing)
