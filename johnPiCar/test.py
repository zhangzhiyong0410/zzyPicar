
import photoelectricSensor
import picar
import time

pls = photoelectricSensor.Photoelectric(16)
pc = picar.Picar(11,12,13,15,37,38,40)

pc.forward(1)

