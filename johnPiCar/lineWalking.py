import picar
import lineWalkingModule

lk = lineWalkingModule.LineWalkingModule(31,32,33,35,36)
pc = picar.Picar(11,12,13,15,37,38,30)

record = 0

while True:

    walkingState = lk.DetectionState()

    #如果巡线状态不是前进指标，那就到前进指标为止
    while walkingState != [1,1,0,1,1]:

        walkingState = lk.DetectionState()

        if walkingState == [1,0,1,1,1] or walkingState == [0,1,1,1,1] or walkingState == [0,0,1,1,1] or walkingState == [0,0,0,1,1]:

            record = 0

            pc.speed = 3.6
            pc.anticlockwise(0)

        elif walkingState == [1,1,1,0,1] or walkingState == [1,1,1,1,0] or walkingState == [1,1,0,0,0] or walkingState == [1,1,1,0,0]:
            
            record = 1

            pc.speed = 30
            pc.clockwise(0)
        
        elif walkingState == [1,1,1,1,1]:

            if record == 0:
            
                pc.speed = 30
                pc.anticlockwise(0)

            else:

                pc.speed = 30
                pc.clockwise(0)

    pc.speed = 15
    pc.forward(0)






