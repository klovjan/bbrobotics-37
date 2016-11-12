from sens_ob import SensOb
from reflectance_sensors import *
class ReflectanceOb(SensOb):
	def __init__(self, rs): #initializes the InfraredSensOb object to house the specified sensor. 
		Sensob.__init__(self, rs)

	def _calculate(): #sets the attribute "value" of the InfraredSensOb object to the current reading of the reflectance sensor reading. 
		self.value = self.sensor.update()
		return self.value
