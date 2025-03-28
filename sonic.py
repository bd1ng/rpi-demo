from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo=12, trigger=5)

while True:
    print('Distance in meters: ', ultrasonic.distance)
    print('Distance in cm: ', (ultrasonic.distance * 34300) / 2)
    print('Distance in feet: ', int((ultrasonic.distance / 0.3048) * 12))
    sleep(0.5)
