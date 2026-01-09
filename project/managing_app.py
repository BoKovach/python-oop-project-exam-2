from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if not self.find_user_by_license(driving_license_number):
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"
        return f"{driving_license_number} has already been registered to our platform."


    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self.find_vehicle_by_license(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = self.find_route(start_point, end_point, length)
        if route:
            return f"{start_point}/{end_point} - {length} {'km' if route.length == length else 'shorter route'}" \
                   f" had already been added to our platform."

        route.route_id = 1 if route.route_id is None else + 1
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."


    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        pass

    def repair_vehicles(self, count: int):
        pass

    def users_report(self):
        pass

    def find_user_by_license(self, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user


    def find_vehicle_by_license(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle


    def find_route(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length <= length:
                return route




