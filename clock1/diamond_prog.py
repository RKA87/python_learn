class ElectricVehicle:
    def __init__(self, battery_capacity:int, charging_time:int):
        self.__battery_capacity = battery_capacity
        self.__charging_time = charging_time

    @property
    def battery_capacity(self):
        return self.__battery_capacity
    
    @battery_capacity.setter
    def battery_capacity(self,battery_capacity):
        self.__battery_capacity=battery_capacity
    
    @property
    def charging_time(self):
        return self.__charging_time
    
    @charging_time.setter
    def charging_time(self,charging_time):
        self.__charging_time=charging_time
    
    def charge_battery(self):
        print("Charging the battery...")

class GasolineVehicle:
    def __init__(self,fuel_tank_capacity, fuel_efficiency):
        self.__fuel_tank_capacity=fuel_tank_capacity
        self.__fuel_efficiency=fuel_efficiency

    @property
    def fuel_tank_capacity(self):
        return self.__fuel_tank_capacity
    
    @fuel_tank_capacity.setter
    def fuel_tank_capacity(self,fuel_tank_capacity):
        self.__fuel_tank_capacity=fuel_tank_capacity
    
    @property
    def fuel_efficiency(self):
        return self.__fuel_efficiency
    
    @fuel_efficiency.setter
    def fuel_efficiency(self,fuel_efficiency):
        self.__fuel_efficiency=fuel_efficiency
    
    def refuel(self):
        print("Refueling Tank...")

class HybridCar(ElectricVehicle,GasolineVehicle):
    def __init__(self,battery_capacity:int,charge_battery:int,fuel_efficiency, fuel_tank_capacity):
        ElectricVehicle.__init__(self,battery_capacity,charge_battery)
        GasolineVehicle.__init__(self,fuel_efficiency, fuel_tank_capacity)
    
    def drive(self):
        print("driving use both electric and gasoline power source")
    
inst=HybridCar(battery_capacity=100,charge_battery=80,fuel_efficiency=80,fuel_tank_capacity="full",)
inst.charge_battery()
inst.refuel()
inst.drive()    

illegal_names = {"Henry", "Oscar"}
print(type(illegal_names))