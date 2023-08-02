from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 180.00)

    def drive(self, mileage: float):
        percent = round(mileage / self.max_mileage * 100)
        self.battery_level -= percent + 5 # it was self.battery_level -= percent * self.battery_level + 5