from project.validators import Validators


class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.driving_license_number = driving_license_number
        self.last_name = last_name
        self.first_name = first_name

        self.rating = 0
        self.is_blocked = False

    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        Validators.check_for_empty_string(value, "First name cannot be empty!")
        self._first_name = value
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        Validators.check_for_empty_string(value, "Last name cannot be empty!")
        self._last_name = value

    @property
    def driving_license_number(self):
        return self._driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        Validators.check_for_empty_string(value, "Driving license number is required!")
        self._driving_license_number = value

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        Validators.check_if_value_lt_zero(value, "Users rating cannot be negative!")
        self._rating = value

    def increase_rating(self):
        self.rating += 0.5
        if self.rating > 10:
            self.rating = 10

    def decrease_rating(self):
        self.rating -= 2
        if self.rating < 0:
            self.rating = 0
            self.is_blocked = True

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"
