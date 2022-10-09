"""
Raspberry Pi Code:
Code Links:
https://github.com/tutRPi/Raspberry-Pi-Gas-Sensor-MQ/blob/master/example.py
https://www.iotstarters.com/connecting-dht11-sensor-with-raspberry-pi-3-4-using-python/

"""

# import os
import time
import sys
from time import sleep

# from multiprocessing import Process
import Adafruit_DHT
import urllib2
from mq import MQ
import RPi.GPIO as GPIO

# The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number
GPIO.setmode(GPIO.BCM)

# Buzzer pin setup
piezo = 18
GPIO.setup(piezo, GPIO.OUT)

# PIR(Motion Sensor) pin setup
pir_sensor = 17
GPIO.setup(pir_sensor, GPIO.IN)

# Setup the pins we are connect to
RCpin = 24
DHTpin = 23

# Thingspeak API Endpoint
myAPI = 'XXXXXXXXXXXXXXXX'


# Time delay between posting data to Thingspeak
myDelay = 15

# GPIO.setmode(GPIO.BCM)
GPIO.setup(RCpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Defining Threshold of Sensors
smoke_threshold = 0.3
temperature_threshold = 30


# current_state = 0  # Think this is not needed.
# DEBUG = 1

def motion():
    """
    Activating Data collection from motion sensor when thresholds are breached.
    :return:
    """
    print("Motion Sensor is Activated.")
    try:
        i = 1
        while i <= 10:
            time.sleep(0.1)
            current_state = GPIO.input(pir_sensor)
            if current_state == 1:
                print("GPIO pin %s is %s" % (pir_sensor, current_state))
                GPIO.output(piezo, True)
                time.sleep(1)
                GPIO.output(piezo, False)
                time.sleep(1)
                i = i + 1
    except KeyboardInterrupt:
        pass


def get_dht11_data():
    """
    Collect Temperature and Humidity Data from DHT11 Sensor.
    :return:
        humidity: humidity as string in grams of moisture per cubic meter of air (g/m3).
        temp_celsius: temperature in celsius
        temp_fahrenheit: temperature in fahrenheit
    """
    humidity, temp_celsius = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    # Convert from Celsius to Fahrenheit
    temp_fahrenheit = 9 / 5 * temp_celsius + 32

    return str(humidity), str(temp_celsius), str(temp_fahrenheit)


def RCtime(RCpin):
    """

    :param RCpin:
    :return:
    """
    LT = 0
    if GPIO.input(RCpin) == True:
        LT += 1

    return str(LT)


print("GAS SENSOR")
print("Press CTRL+C to abort.")

mq = MQ()

while True:
    # Running Smoke Detection and Temperature Detection continuously till either one of then cross given threshold.
    try:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO2: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
        a = float(perc["SMOKE"])
        if a > 0.3:
            print("Smoke crossed the threshold of {0} ppm. Activating Motion Sensor...".format(smoke_threshold))
            motion()
        sys.stdout.flush()
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAborted by User")

    # Uploading Sensor Data to Thingspeak
    try:
        print('\n Sending to thingspeak...')
        baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
        humidity, temp_celsius, temp_fahrenheit = get_dht11_data()
        LT = RCtime(RCpin)
        f = urllib2.urlopen(baseURL +
                            "&field1=%s&field2=%s&field3=%s" % (temp_celsius, temp_fahrenheit, humidity) +
                            "&field4=%s&field5=%s&field6=%s" % (perc["CO"], perc["SMOKE"], LT)
                            )
        print(f.read())
        print(temp_celsius + " " + temp_fahrenheit + " " + humidity + " " + LT)
        tem = float(temp_celsius)
        if tem >= temperature_threshold:
            print("Temperature crossed the given threshold of {0} Celsius. Activating motion sensor...".
                  format(temperature_threshold))
            motion()
        f.close()
        sleep(myDelay)
    except KeyboardInterrupt:
        print('Exiting...')
