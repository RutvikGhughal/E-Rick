import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)  #LED to GPIO24
GPIO.output(24, True)
time.sleep(3)
GPIO.output(24, False)
time.sleep(2)