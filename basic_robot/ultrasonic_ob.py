from sens_ob import SensOb
class UltrasonicOb(SensOb):
	def __init__(self, us):
		SensOb.__init__(us)
	def _calculate(self):
		self.value = self.sensor.update()
		return self.value