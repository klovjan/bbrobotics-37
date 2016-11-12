from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic
from camera import Camera
from irproximity_sensor import IRProximitySensor
from zumo_button import ZumoButton


class Sensob:
    def __init__(self, sensor):  # Initializes the SensOb object to house the different SWs.
        self.sensor = sensor

    def update(self):
        return self._calculate()

    def _calculate(self):  # Calculates relevant data from the SWs.
        pass


class ReflectanceSensorsSensob(Sensob):
    def __init__(self, rs):  # Initializes the InfraredSensOb object to house the specified sensor.
        super().__init__(rs)

    def _calculate(self):  # Sets the attribute "value" of the InfraredSensOb object to the current reading of the reflectance sensor reading.
        self.value = self.sensor.update()
        return self.value


class UltrasonicSensob(Sensob):
    def __init__(self, us):
        super().__init__(us)

    def _calculate(self):
        self.value = self.sensor.update()
        return self.value


class CameraSensob(Sensob):
    def __init__(self, sensor):
        super().__init__(sensor)

    def _calculate(self):
        super()._calculate()


class IRProximitySensorSensob(Sensob):
    def __init__(self, sensor):
        super().__init__(sensor)

    def _calculate(self):
        super()._calculate()


class ZumoButtonSensob(Sensob):
    def __init__(self, sensor):
        super().__init__(sensor)

    def _calculate(self):
        super()._calculate()
