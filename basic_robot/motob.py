from motors import Motors


class Motob:
    value = None
    motors = None

    def __init__(self):
        self.motors = Motors()

    def update(self, value):
        self.value = value
        self.operationalize(self.value)

    def operationalize(self, rec):
        eval("self." + rec)

    # go_direction is a funciton to make the robot go a certain direction, with a certain speed and duration
    # Valid directions are: "forward", "backward"
    # Valid speeds are  : [-1.0, 1.0]
    # Valid durations are :  dur >= 0
    def go_direction(self, dir='forward', dur=None, speed=0):
        try:
            eval('self.motors.' + dir)(speed, dur)
        except:
            if dur < 0:
                print(str(dur) + " is not a valid duration")
            elif speed < -1.0 or speed > 1.0:
                print(str(speed)+ " is not a valid speed")
            else:
                print(dir + " is not a valid direction")

    # Turn_direction is a function to make the robot turn a certain direction, for a certain time, with a certain speed
    def turn_direction(self, dir="left", dur=None, speed=0):
        try:
            eval('self.motors.' + dir)(speed, dur)
            print("finished")
        except:
            if dur < 0:
                print(str(dur) + " is not a valid duration")
            elif speed < -1.0 or speed > 1.0:
                print(str(speed) + " is not a valid speed")
            else:
                print(dir + " is not a valid direction")
