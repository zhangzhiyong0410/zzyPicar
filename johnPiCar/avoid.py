import photoelectricSensor
import picar

pls = photoelectricSensor.Photoelectric(16)
pc = picar.Picar(11,12,13,15,37,38,20)

while True:

    barrier = pls.obstacleDetection()
    if barrier == 0:
        pc.speed = 40
        pc.anticlockwise(0.5)
    else:
        pc.speed = 20
        pc.forward(0)
