"""
AIPI 590
WEEK 4 - LAB 1
___________________
DHT11 TEMPERATURE AND HUMIDITY SENSOR

- Clone this code to your Raspberry Pi
- Complete the required function to read data from the DHT11 sensor
- Save temperature and humidity data to a CSV file
- Push back to Edstem with Git

"""

import adafruit_dht
import board
import time
import csv
import os

# SETUP GPIO MODE AND SENSOR
# The SENSOR_PIN variable will point to the GPIO pin
# using the Adafruit 'board' library. The pin # will be preceeded with 'D'
SENSOR_PIN = 26
# Create a variable for the DHT11 sensor
sensor = adafruit_dht.DHT11(board.D26)

# CSV FILE SETUP
# Creates a name for the CSV file
CSV_FILE = "dht11_data.csv"
# Sets up the columns (fields) for the CSV file
FIELDNAMES = ["Timestamp", "Temperature (C)", "Humidity (%)"]

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""


def read_sensor_data():

    """    
    Reads data from the DHT11 sensor.
    - Read the temperature and store it as a variable called 'temperature'
    - Read the humidity and store it as a variable called 'humidity'
    Check to see if the readings are empty
    - Use an 'if ... is None' statement to check for empty values
    - If there are empty values, print an error. 
    - Else, print out the temerature and humidy readings.

    Returns temperature and humidity as a tuple.
    """
    ### BEGIN SOLUTION ###

    while True:
        temperature = sensor.temperature
        humidity = sensor.humidity
        if humidity is None or temperature is None:
            print("Sensor failure. Check wiring.")
        else:
            print(f'\nTemp in C: {temperature}\nHumidity: {humidity}\n____________________')
        time.sleep(2)
    
    ### END SOLUTION ###
    return temperature, humidity
    

def write_data_to_csv(file_path, temperature, humidity):
    """
    Writes temperature and humidity data to the CSV file.
    - Create a variable that checks to see if the file already exists
    - Create a timestamp variable called 'timestamp'
    - Open the csv file
    - Create a 'writer' variable to write the fieldnames
    - If the file does not exist, it initializes the file with headers.
    - Otherwise, write the new row that includes this data:
        - Timestamp
        - Temp
        - Humidity
    """
    file_exists = os.path.exists(file_path)
    ### BEGIN SOLUTION ###
    

    ### END SOLUTION ###



"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
ANY CODE BELOW THIS LINE
___________________
"""


def main():
    """
    Main function to read sensor data and log it to a CSV file.
    """
    print("Starting DHT11 Sensor Logging...")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            try:
                # Use the solution function to read data
                temperature, humidity = read_sensor_data()
                # Log data to the CSV file
                write_data_to_csv(CSV_FILE, temperature, humidity)

            except RuntimeError as e:
                # Handle intermittent sensor reading errors
                print(f"Reading error: {e}")

            # Wait before the next reading
            time.sleep(2)

    except KeyboardInterrupt:
        print("Exiting program. Goodbye!")
    finally:
        sensor.exit()


# Run the main function
if __name__ == "__main__":
    main()

