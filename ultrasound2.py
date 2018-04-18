import RPi.GPIO as GPIO

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#trig -11 and echo -13
print "Distance Measurement In Progress"

GPIO.setup(11,GPIO.OUT)

GPIO.setup(13,GPIO.IN)
while (True):
   GPIO.output(11, False)

   print "Waiting For Sensor To Settle"

   time.sleep(0.1)


   GPIO.output(11, True)

   time.sleep(0.00001)

   GPIO.output(11, False)

   while GPIO.input(13)==0:

     pulse_start = time.time()

   while GPIO.input(13)==1:

      pulse_end = time.time()

   pulse_duration = pulse_end - pulse_start

   distance = pulse_duration * 17150

   distance = round(distance, 2)
   distance = distance + 1  #there is 1 cm gap in the real calculation
   print "Distance:",distance,"cm"

   if distance<1:
              #print "obstcle on right", i
                GPIO.output(40,1)
                GPIO.output(38,0)
                GPIO.output(35,1)
                GPIO.output(37,0)
   else :                             #Right IR sensor detects an object
                GPIO.output(40,0)
                GPIO.output(38,1)
                GPIO.output(35,0)
                GPIO.output(37,1)
