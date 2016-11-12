# The main behavior class, which contains the basic functions standard to the behavior
class Behavior:
    # Initializing most values
    def __init__(self, bbcon, sensobs, priority, active_flag=False, halt_request=False):
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.priority = priority
        self.active_flag = active_flag
        self.halt_request = halt_request
        self.match_degree = 0
        self.weight = self.match_degree * self.priority

        self.motor_recommendations = None

    # Is called every cycle to check if the behavior should be allowed to activate
    def consider_deactivation(self):
        pass

    # Is called every cycle to check if the behavior
    def consider_activation(self):
        pass

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        # If the behavior is (still) active:
        if self.active_flag:
            self.sense_and_act()
            self.weight = self.get_match_degree() * self.priority

    def get_match_degree(self):
        pass

    def sense_and_act(self):
        pass

    def _activate(self):
        self.active_flag = True

    def _deactivate(self):
        self.active_flag = False


class Attack(Behavior):
    def __init__(self, bbcon, sensobs, priority, active_flag=False, halt_request=False):
        Behavior.__init__(self, bbcon, sensobs, priority, active_flag=False, halt_request=False)

    def consider_activation(self):
        if self.bbcon.arbitrator.last_behavior == 0:
            self._activate()

    def consider_deactivation(self):
        if self.bbcon.arbitrator.last_behavior == 2:
            self._deactivate()

    def get_match_degree(self):
        sensor = sensobs[0]
        sensor.update()
        distance = sensor.get_value()
        if distance > 5:
            self.match_degree = 0
            return self.match_degree
        else:
            self.match_degree = abs(distance - 5)/5
            return self.match_degree

    def sense_and_act(self):
        self.motor_recommendations = ["go_direction('forward', 1.0, 0.1)"]


# Behavior which handles patrolling along duct-tape
class Patrol(Behavior):
    def __init__(self, bbcon, sensobs, priority, active_flag=False, halt_request=False):
        Behavior.__init__(self, bbcon, sensobs, priority, active_flag=False, halt_request=False)

    def consider_activation(self):
        if self.bbcon.arbitrator.last_behavior == 3:
            self._activate()

    def consider_deactivation(self):
        if self.bbcon.arbitrator.last_behavior == 1:
            self._deactivate()

    def get_match_degree(self):
        sensor = self.sensobs[0]
        if sum(sensor) > 1.5 and max(sensor) - min(sensor) < 0.25:
            self.match_degree = 0
            return self.match_degree
        elif sum(sensor) > 1.5 and max(sensor) - min(sensor) < 0.25:
            line_pos = self._get_line_pos()
            if line_pos == -1:
                self.match_degree = 0
                return self.match_degree
            self.match_degree = abs(line_pos - 2.5)/2.5
        else:
            self.match_degree = 1.0
            return self.match_degree

    def _get_line_pos(self):
        sensor = self.sensobs[0]
        left = None
        right = None
        for i in range(sensor):
            if sensor[i] < 0.2:
                left = i
                break
        for o in range(sensor):
            if sensor[sensor.__len__() - 1 - o] < 0.2:
                right = o
                break

        if left is not None and right != right:
            return (left + right) / 2
        else:
            return -1

    def sense_and_act(self):
        line_pos = self._get_line_pos()
        if line_pos < 2.5:
            self.motor_recommendations = ["turn_direction('left'," + str(abs(line_pos - 2.5)/2.5) + ", 0.1)"]
        elif line_pos > 2.5:
            self.motor_recommendations = ["turn_direction('right'," + str(abs(line_pos - 2.5) / 2.5) + ", 0.1)"]
        else:
            self.motor_recommendations = ["go_direction('forward', 1.0, 0.1"]
