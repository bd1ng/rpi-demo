"""
AIPI 590
WEEK 4 - LAB 2
___________________
HC-SR04 ULTRASONIC DISTANCE SENSOR

- Clone this code to your Raspberry Pi
- Complete the required function to measure distance
- Save distance readings to the console
- Push back to Edstem with Git

"""

from gpiozero import DistanceSensor
from time import sleep

"""
PIN CONFIGURATION:
Setup GPIO pins for trigger and echo
"""

TRIGGER_PIN = 23 
ECHO_PIN = 24

"""
SENSOR CONFIGURATION:
Configure the distance sensor using the GPIO variables
"""
ultrasonic = DistanceSensor(echo=ECHO_PIN, trigger=TRIGGER_PIN)

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""


def measure_distance(sensor):
    """
    Measures the distance using the HC-SR04 sensor.
    - Create variables for meters, feet, and centimeters.
    - Print out those variables to the console.
    """
    ### BEGIN SOLUTION ###

    meters = ultrasonic.distance
    cm = (ultrasonic.distance * 34300) / 2
    ft = int(ultrasonic.distance / 0.3048) * 12

    print('Distance in meters: ', meters)
    print('Distance in cm: ', cm)
    print('Distance in feet: ', ft)
    sleep(0.5)


    ### END SOLUTION ###


"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
ANY CODE BELOW THIS LINE
___________________
"""


def main():
    """
    Main function to initialize the HC-SR04 sensor and continuously measure distance.
    """
    print("Starting HC-SR04 Ultrasonic Distance Sensor...")
    print("Press Ctrl+C to stop.")

    # Initialize the ultrasonic distance sensor
    try:
        while True:
            # Use the solution function to measure distance
            measure_distance(ultrasonic)
            # Wait before the next reading
            sleep(1)

    except KeyboardInterrupt:
        print("Exiting program. Goodbye!")


# Run the main function
if __name__ == "__main__":
    main()

