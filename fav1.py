import RPi.GPIO as GPIO
import time
import curses

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)                            #Right sensor connection
GPIO.setup(5, GPIO.OUT) #Left sensor connection
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.IN)

p=0
while True:
                    
          GPIO.output(11, False)

          print "Waiting For Sensor To Settle"

          time.sleep(0.15)     #change from 5 should not be less than 0.1 or greater than 3


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

          if   (distance<80):
              
                GPIO.output(40,0)
                GPIO.output(38,0)
                GPIO.output(35,0)
                GPIO.output(37,0)

          elif   ((distance<10)and(p==1)):
              #print "obstcle on right", i
                p=0
                GPIO.output(40,0)
                GPIO.output(38,1)
                GPIO.output(35,1)
                GPIO.output(37,0)

                time.sleep(0.4)

                GPIO.output(40,0)
                GPIO.output(38,1)
                GPIO.output(35,0)
                GPIO.output(37,1)
                
          elif   ((distance<10)and(p==0)):
              #print "obstcle on right", i
                p=1
                GPIO.output(40,1)
                GPIO.output(38,0)
                GPIO.output(35,0)
                GPIO.output(37,1)

                time.sleep(0.4)

                GPIO.output(40,0)
                GPIO.output(38,1)
                GPIO.output(35,0)
                GPIO.output(37,1)
          elif j==1:
              #print "obstcle on right", i
                p=1
                GPIO.output(40,0)
                GPIO.output(38,1)
                GPIO.output(35,1)
                GPIO.output(37,0)

          elif i==1:
              #print "obstcle on left", j
                p=0
                GPIO.output(40,1)
                GPIO.output(38,0)
                GPIO.output(35,0)
                GPIO.output(37,1)

          elif i==0:                              #Right IR sensor detects an object
                GPIO.output(40,0)
                GPIO.output(38,1)
                GPIO.output(35,0)
                GPIO.output(37,1)
               #print "ok i",i
               #time.sleep(0.1)
          elif j==0:                              #Left IR sensor detects an object
               print "ok j",j
               time.sleep(0.1)
