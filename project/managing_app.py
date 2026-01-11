from project.route import Route
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
        route_id = max([r.route_id for r in self.routes], default=0) + 1
        same_routes = self.find_same_routes(start_point, end_point)

        if same_routes and any(route.length == length for route in same_routes):
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if same_routes and any(route.length < length for route in same_routes):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        if same_routes:
            self.lock_route(same_routes, length)

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."


    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self.find_user_by_license(driving_license_number)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = self.find_vehicle_by_license(license_plate_number)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = self.find_route_by_id(route_id)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number}" \
               f" Battery: {int(vehicle.battery_level)}% Status: {vehicle.status}"

    def repair_vehicles(self, count: int):
        damaged_vehicles = self.find_damaged_vehicles(count)
        sorted_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))

        for vehicle in sorted_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        sorted_users = sorted(self.users, key=lambda u: u.rating, reverse=True)

        for user in sorted_users:
            result.append(user.__str__())

        return '\n'.join(result).strip()



    def find_user_by_license(self, driving_license_number):
        return next((u for u in self.users if u.driving_license_number == driving_license_number), None)

    def find_vehicle_by_license(self, license_plate_number):
        return next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)

    def find_route_by_id(self, route_id):
        return next((r for r in self.routes if r.route_id == route_id), None)

    def find_same_routes(self, start_point, end_point):
        routes = []
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                routes.append(route)

        if routes:
            return routes
        return []

    @staticmethod
    def lock_route(same_routes, length):
        for route in same_routes:
            if route.length > length:
                route.is_locked = True

    def find_damaged_vehicles(self, count):
        vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged][:count]
        if vehicles:
            return vehicles
        return []





