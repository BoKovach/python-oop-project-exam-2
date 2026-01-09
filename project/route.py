from project.validators import Validators


class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.route_id = route_id
        self.length = length
        self.end_point = end_point
        self.start_point = start_point

        self.is_locked = False

    @property
    def start_point(self):
        return self._start_point
    
    @start_point.setter
    def start_point(self, value):
        Validators.check_for_empty_string(value, "Start point cannot be empty!")
        self._start_point = value

    @property
    def end_point(self):
        return self._end_point

    @end_point.setter
    def end_point(self, value):
        Validators.check_for_empty_string(value, "End point cannot be empty!")
        self._end_point = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        Validators.check_if_value_lt_1(value, "Length cannot be less than 1.00 kilometer!")
        self._length = value

