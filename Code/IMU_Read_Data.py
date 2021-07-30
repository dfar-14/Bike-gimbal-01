# This code is for the purpose of reading data from the ICM-20948 IMU
# The code uses SPI to communicate with the device and saves the data to a file
# This code is meant to integrate with a raspberry pi

#import modules
import spidev
import time

#initialise SPIDev
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 125000
time.sleep(0.0005)


