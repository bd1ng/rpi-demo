import time
import board
import busio
import adafruit_adxl34x

# Setup I2C connection
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADXL345 sensor
sensor = adafruit_adxl34x.ADXL345(i2c, address=0x53)

# Set range (Optional: 2G, 4G, 8G, 16G)
sensor.range = adafruit_adxl34x.Range.RANGE_2_G

def read_adxl345_data():
    """ Reads acceleration data from ADXL345 and prints it """
    x, y, z = sensor.acceleration  # Get acceleration values in m/s²

    print(f"X Acceleration: {x:.2f} m/s²")
    print(f"Y Acceleration: {y:.2f} m/s²")
    print(f"Z Acceleration: {z:.2f} m/s² (should be ~9.8 m/s² due to gravity)")
    print("-" * 30)

# Main loop
try:
    while True:
        read_adxl345_data()
        time.sleep(1)  # Wait 1 second before the next reading
except KeyboardInterrupt:
    print("Exiting program. Goodbye!")