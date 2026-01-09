from abc import ABC, abstractmethod

from project.validators import Validators


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.max_mileage = max_mileage
        self.license_plate_number = license_plate_number
        self.model = model
        self.brand = brand

        self.battery_level = 100
        self.is_damaged = False

        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        Validators.check_for_empty_string(value, "Brand cannot be empty!")
        self._brand = value
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        Validators.check_for_empty_string(value, "Model cannot be empty!")
        self._model = value
        
    @property
    def license_plate_number(self):
        return self._license_plate_number
    
    @license_plate_number.setter
    def license_plate_number(self, value):
        Validators.check_for_empty_string(value, "License plate number is required!")
        self._license_plate_number = value

    @property
    def status(self):
        return 'Ok' if not self.is_damaged else 'Damaged'

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = True if self.is_damaged == False else False

    def __str__(self):
        return f"{self.brand} {self.model} License plate: {self.license_plate_number}" \
               f" Battery: {self.battery_level}% Status: {self.status}"