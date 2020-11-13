import RPi.GPIO as GPIO
import time
trig = 17
echo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setwarnings(False)

print("Start")
try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.5)
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        while GPIO.input(echo) == False:
            pulse_start = time.time()
        while GPIO.input(echo) == True:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)
        print("distance : ", distance, "cm")
except KeyboardInterrupt:
    GPIO.cleanup()