from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)


    def drive(self, mileage: float):
        used_percentage = round(mileage / self.MAX_MILEAGE * 100)
        self.battery_level -= used_percentage
        if self.battery_level < 0:
            self.battery_level = 0