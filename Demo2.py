import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

time.sleep(3)


drone.take_off(10.0)
#drone.position_set_global(37.4196,-122.0782,rel_ht=10.0)
#assuming an equilateral triangle of 10m, height of triangle will be 8.66m,
#hence middle nav point will be at 8.66
print 'point 1'
drone.position_set(10, 0, 0, relative=True, tolerance=0.01, async=False)

print 'point 2'
drone.position_set(-5, 8.66, 0, relative=True, tolerance=0.01, async=False)

print ' point 3'
drone.position_set(-5, -8.66, 0, relative=True, tolerance=0.01, async=False)



print 'Landing'
#due to drone not landing completely, rtl is used
drone.rtl()
time.sleep(50)
drone.disarm()
# shutdown the instance
drone.disconnect()
