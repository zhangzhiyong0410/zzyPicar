import RPi.GPIO as GPIO
import time

#使用BOARD模式
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

class Picar:

    def __init__(self,l298nPin1,l298nPin2,l298nPin3,l298nPin4,EnableA,EnableB,speed):

        self.l298nPin1 = l298nPin1
        self.l298nPin2 = l298nPin2
        self.l298nPin3 = l298nPin3
        self.l298nPin4 = l298nPin4

        self.EnableA = EnableA
        self.EnableB = EnableB
        self.speed = speed

        GPIO.setup(self.l298nPin1,GPIO.OUT)
        GPIO.setup(self.l298nPin2,GPIO.OUT)
        GPIO.setup(self.l298nPin3,GPIO.OUT)
        GPIO.setup(self.l298nPin4,GPIO.OUT)

        GPIO.setup(self.EnableA,GPIO.OUT)
        GPIO.setup(self.EnableB,GPIO.OUT)

        self.pwmA = GPIO.PWM(self.EnableA,50)
        self.pwmB = GPIO.PWM(self.EnableB,50)

        self.pwmA.start(0)
        self.pwmB.start(0)

    #调速
    def speedGoverning(self):

        self.pwmA.ChangeDutyCycle(self.speed)
        self.pwmB.ChangeDutyCycle(self.speed)

    #延迟
    def ywzq(self,yanshi):
        if yanshi > 0:
            time.sleep(yanshi)
        else:
            pass

    #向前
    def forward(self,yanshi):

        GPIO.output(self.l298nPin1,GPIO.LOW)
        GPIO.output(self.l298nPin2,GPIO.HIGH)
        GPIO.output(self.l298nPin3,GPIO.LOW)
        GPIO.output(self.l298nPin4,GPIO.HIGH)

        self.speedGoverning()
        self.ywzq(yanshi)

    #向后
    def backwards(self,yanshi):

        GPIO.output(self.l298nPin1,GPIO.HIGH)
        GPIO.output(self.l298nPin2,GPIO.LOW)
        GPIO.output(self.l298nPin3,GPIO.HIGH)
        GPIO.output(self.l298nPin4,GPIO.LOW)

        self.speedGoverning()
        self.ywzq(yanshi)
    
    #向左边
    def turnLeft(self,yanshi):

        GPIO.output(self.l298nPin1,GPIO.LOW)
        GPIO.output(self.l298nPin2,GPIO.LOW)
        GPIO.output(self.l298nPin3,GPIO.LOW)
        GPIO.output(self.l298nPin4,GPIO.HIGH)
        self.speedGoverning()
        self.ywzq(yanshi)
        

    #向右转
    def turnRight(self,yanshi):

        GPIO.output(self.l298nPin3,GPIO.LOW)
        GPIO.output(self.l298nPin4,GPIO.LOW)
        GPIO.output(self.l298nPin1,GPIO.LOW)
        GPIO.output(self.l298nPin2,GPIO.HIGH)
        self.speedGoverning()
        self.ywzq(yanshi)

    #自转右
    def clockwise(self,yanshi):

        GPIO.output(self.l298nPin1,GPIO.LOW)
        GPIO.output(self.l298nPin2,GPIO.HIGH)
        GPIO.output(self.l298nPin3,GPIO.HIGH)
        GPIO.output(self.l298nPin4,GPIO.LOW)
        
        self.speedGoverning()
        self.ywzq(yanshi)

    #自转左
    def anticlockwise(self,yanshi):

        GPIO.output(self.l298nPin1,GPIO.HIGH)
        GPIO.output(self.l298nPin2,GPIO.LOW)
        GPIO.output(self.l298nPin3,GPIO.LOW)
        GPIO.output(self.l298nPin4,GPIO.HIGH)

        self.speedGoverning()
        self.ywzq(yanshi)

    #停止
    def stop(self):

        GPIO.output(self.l298nPin1,GPIO.LOW)
        GPIO.output(self.l298nPin2,GPIO.LOW)
        GPIO.output(self.l298nPin3,GPIO.LOW)
        GPIO.output(self.l298nPin4,GPIO.LOW)


def test():

    l298nPin1 = 11
    l298nPin2 = 12
    l298nPin3 = 13
    l298nPin4 = 15
    EnableA = 37
    EnableB = 38
    speed = 20

    GPIO.setup(l298nPin1,GPIO.OUT)
    GPIO.setup(l298nPin2,GPIO.OUT)
    GPIO.setup(l298nPin3,GPIO.OUT)
    GPIO.setup(l298nPin4,GPIO.OUT)

    GPIO.setup(EnableA,GPIO.OUT)
    GPIO.setup(EnableB,GPIO.OUT)

    pwmA = GPIO.PWM(EnableA,50)
    pwmB = GPIO.PWM(EnableB,50)

    pwmA.start(0)
    pwmB.start(0)    

    GPIO.output(l298nPin1,GPIO.LOW)
    GPIO.output(l298nPin2,GPIO.HIGH)
    GPIO.output(l298nPin3,GPIO.LOW)
    GPIO.output(l298nPin4,GPIO.HIGH)
    
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)

    time.sleep(1)

    GPIO.output(l298nPin1,GPIO.LOW)
    GPIO.output(l298nPin2,GPIO.LOW)
    GPIO.output(l298nPin3,GPIO.LOW)
    GPIO.output(l298nPin4,GPIO.LOW)

    GPIO.cleanup()

if __name__ == '__main__':
    i = Picar(11,12,13,15,37,38,30)
    i.turnRight(1)


