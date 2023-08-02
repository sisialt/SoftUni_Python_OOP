from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def find_user(self, driving_license_number):
        user = [u for u in self.users if u.driving_license_number == driving_license_number]
        if user:
            return user[0]
        return None

    def find_vehicle(self, license_plate_number):
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]
        if vehicle:
            return vehicle[0]
        return None

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.find_user(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in BaseVehicle.VALID_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self.find_vehicle(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == "PassengerCar":
            vehicle = PassengerCar(brand, model, license_plate_number)
        elif vehicle_type == "CargoVan":
            vehicle = CargoVan(brand, model, license_plate_number)

        self.vehicles.append(vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length == length]
        if route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length < length]
        if route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)

        longer_route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length > length]
        if longer_route:
            # for l_r in longer_route:  # marker if there are more than 1 longer routes
            longer_route[0].is_locked = True

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self.find_user(driving_license_number)
        vehicle = self.find_vehicle(license_plate_number)
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([v for v in self.vehicles if v.is_damaged], key=lambda x: (x.brand, x.model))
        if count < len(damaged_vehicles):
            damaged_vehicles = damaged_vehicles[:count]  # it was count + 1

        for vehicle in damaged_vehicles:
            vehicle.change_status()
            vehicle.recharge()

        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"


    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        result = '\n'.join([str(u) for u in sorted_users])
        return (f"*** E-Drive-Rent ***\n"
                f"{result}")