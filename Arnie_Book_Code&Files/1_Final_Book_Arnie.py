import RPi.GPIO as GPIO
import time
import os

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN) ###Button 1
GPIO.setup(4, GPIO.IN) ###Button 2
GPIO.setwarnings(False)##switch off other ports

playing = True

from gpiozero import LED
led = LED(17)
led.off()

def terminator_eye():
    
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

global distance

GPIO.setmode(GPIO.BCM)

TRIG = 23 #pin 
ECHO = 24 #pin
print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

###Find distance###
def How_Far_Away():
    global distance
    GPIO.output(TRIG, False)
    print ("Waiting for sensor to settle")
    time.sleep(1)

    GPIO.output(TRIG, True)

    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)== 0:
        pulse_start=time.time()
        
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
       
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print (distance)

    print("Distance:", distance,"cm")
    return distance

    GPIO.cleanup()

time.sleep(10)
    
while True:
        while GPIO.input(25) == 1 and GPIO.input(4) == 1:
                    print("Up")
                    led.off()
                    How_Far_Away()
                    distance = int(distance)
                    print (distance)
                    print (type(distance))

                    ###Sort out the values
                    if distance < 50:
                        os.system('cvlc pickmeoffshelf.mp3 &')
                        time.sleep(3)
                        # eye flash test
                        #terminator_eye()
                    elif distance < 100:
                        os.system('cvlc fooling_around.mp3 &')
                        time.sleep(3)
                    elif distance > 100 < 150:
                        os.system('cvlc overhere2.mp3 &')
                        time.sleep(3)
                    elif distance > 151 < 200:
                        os.system('cvlc overhere.mp3 &')
                        time.sleep(3)
                    else:
                        pass
                    
                    time.sleep(3)
                       ###back cover 
                    if GPIO.input(25) == 0 and GPIO.input(4) == 1:
                        os.system('cvlc a.mp3 &')
                        time.sleep(3)
                        os.system('cvlc a2.mp3 &') ###hello my name is
                        time.sleep(6)
                        os.system('cvlc a3.mp3 &') ###turn to the back cover
                        time.sleep(3)

                        time.sleep(5)
                        
                        if GPIO.input(25) == 1 and GPIO.input(4) == 0:
                                print("Right")
                                os.system('cvlc a6.mp3 &') ##did not belive me
                                time.sleep(4.5)
                                os.system('cvlc t2.mp3 &')  #t2theme
                                time.sleep(5)
                                os.system('cvlc a5.mp3 &')
                                led.on()
                                time.sleep(4)
                                terminator_eye() #flash eye
                                os.system('cvlc backontheshelf.mp3 &')
                                time.sleep(4)
                                os.system('cvlc backontheshelf.mp3 &')
                                time.sleep(4)
                                if GPIO.input(25) == 1 and GPIO.input(4) == 1:
                                        os.system('cvlc thankyou.mp3 &')
                                        time.sleep(4)
                                        pass
                                

                                    
                        else: ##does not turn book over
                                
                                os.system('cvlc a4.mp3 &') ## make me angry
                                time.sleep(3)
                                led.on()
                                os.system('cvlc t2.mp3 &')  #t2theme
                                
                                time.sleep(10)
                                os.system('cvlc live.mp3 &')
                                ###kill music
                                time.sleep(2)
                                #os.system('cvlc approach.mp3')
                                time.sleep(3)
                                os.system('cvlc baby.mp3 &')
                                time.sleep(2)
                                #os.system('cvlc gettothe.mp3 &')
                                print("TEST")
                                os.system('cvlc backontheshelf.mp3 &')
                                time.sleep(4)
                                os.system('cvlc backontheshelf.mp3 &')
                                print ("put me back on the shelf")
                                time.sleep(3)                                
                                if GPIO.input(25) == 1 and GPIO.input(4) == 1:
                                        os.system('cvlc thankyou.mp3 &')
                                        time.sleep(4)
                                        pass
                                
                                #pass
                                
        else:
                continue
                print("not ready")

                        

                                


                        
                    
                        
                 
            


