import random
import string

class VehicleInfo:
    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price
    
    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric :
            tax_percentage = 0.02
        return tax_percentage*self.catalogue_price
    
    def print(self):
        print(f'Brand: {self.brand}')
        print(f'Payable tax: {self.compute_tax()}')
    

class Vehicle:
    def __init__(self, id, licence_plate, info):
        self.id = id
        self.licence_plate = licence_plate
        self.info = info
    def print(self):
        print(f'ID: {self.id}')
        print(f'Licence Plate: {self.licence_plate}')
        self.info.print()
    
class VehicleRegistry:
    def __init__(self):
        self.VehicleInfo ={}
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)
    
    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.VehicleInfo[brand] = VehicleInfo(brand, electric, catalogue_price)
    
    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_vehicle_licence(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"
    
    def create_vehicle(self, brand):
        id = self.generate_vehicle_id(12)
        licence_plate = self.generate_vehicle_licence(id)
        return Vehicle(id, licence_plate, self.VehicleInfo[brand])
        
class Application:

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()
        vehicle = registry.create_vehicle(brand)

        vehicle.print()

app = Application()
app.register_vehicle('Volkswagen ID3')