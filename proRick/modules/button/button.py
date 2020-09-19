import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(20, GPIO.OUT)  #LED to GPIO24
flag = 0

try:
    while True:
         button_state = GPIO.input(21)
         if button_state == False :
	     if flag == 0:
                GPIO.output(20, True)
                print('Button Pressed...')
		flag = 1
	     else:
		flag = 0
		GPIO.output(20,False)
	     time.sleep(0.2)
except:
    print("error")
    GPIO.cleanup()
