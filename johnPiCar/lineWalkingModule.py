import RPi.GPIO as GPIO
import time


#使用BOARD模式
GPIO.setmode(GPIO.BOARD)

class LineWalkingModule:

    def __init__(self,lkPin1,lkPin2,lkPin3,lkPin4,lkPin5):

        self.lkPin1 = lkPin1
        self.lkPin2 = lkPin2
        self.lkPin3 = lkPin3
        self.lkPin4 = lkPin4
        self.lkPin5 = lkPin5

        GPIO.setup(self.lkPin1,GPIO.IN)
        GPIO.setup(self.lkPin2,GPIO.IN)
        GPIO.setup(self.lkPin3,GPIO.IN)
        GPIO.setup(self.lkPin4,GPIO.IN)
        GPIO.setup(self.lkPin5,GPIO.IN)
    
    def DetectionState(self):

        startGroup = [0,0,0,0,0]

        startGroup[0] = GPIO.input(self.lkPin1)
        startGroup[1] = GPIO.input(self.lkPin2)
        startGroup[2] = GPIO.input(self.lkPin3)
        startGroup[3] = GPIO.input(self.lkPin4)
        startGroup[4] = GPIO.input(self.lkPin5)

        return startGroup


def test():

    lkPin1 = 31
    lkPin2 = 32
    lkPin3 = 33
    lkPin4 = 35
    lkPin5 = 36

    GPIO.setup(lkPin1,GPIO.IN)
    GPIO.setup(lkPin2,GPIO.IN)
    GPIO.setup(lkPin3,GPIO.IN)
    GPIO.setup(lkPin4,GPIO.IN)
    GPIO.setup(lkPin5,GPIO.IN)    

    startGroup = [0,0,0,0,0]

    while True:

        time.sleep(0.5)

        startGroup[0] = GPIO.input(lkPin1)
        startGroup[1] = GPIO.input(lkPin2)
        startGroup[2] = GPIO.input(lkPin3)
        startGroup[3] = GPIO.input(lkPin4)
        startGroup[4] = GPIO.input(lkPin5)

        print(startGroup)

if __name__ == '__main__':
    test()




