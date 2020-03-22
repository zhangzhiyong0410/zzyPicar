import RPi.GPIO as GPIO
import time

#使用bcm模式
GPIO.setmode(GPIO.BOARD)

class Photoelectric:
    
    #irPin:引脚
    def __init__(self,irPin):
        self.irPin = irPin

    #返回障碍物状态
    def obstacleDetection(self):
        
        GPIO.setup(self.irPin,GPIO.IN)
        statusId = GPIO.input(self.irPin)
        print(statusId)
        return statusId


def test():

    #定义红外模块的引脚为16
    infrared = 16

    #定义红外模块引脚位输入引脚
    GPIO.setup(infrared,GPIO.IN)

    while True:
        status = GPIO.input(infrared)
        time.sleep(0.5)
        if(status == 1):
            print("无-----前方没有障碍物")
        else:
            print("有-----前方出现障碍物")

if __name__ == '__main__':
    test()