import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

time.sleep(3)


drone.take_off(5.0)
#drone.position_set_global(rel_ht=5.0)
#making a square of side length 6.5m
print 'point 1'
drone.position_set(6.5, 0, 0, relative=True, tolerance=0.01, async=False)

print 'point 2'
drone.position_set(0, 6.5, 0, relative=True, tolerance=0.01, async=False)

print ' point 3'
drone.position_set(-6.5, 0, 0, relative=True, tolerance=0.01, async=False)

print 'point 4'
drone.position_set(0, -6.5, 0, relative=True, tolerance=0.01, async=False)

print 'Landing'
drone.rtl()

# shutdown the instance
drone.disconnect()
