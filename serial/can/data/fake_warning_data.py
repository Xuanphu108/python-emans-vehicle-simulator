import array
from serial.can.data.tire import Tire


class FakeWarningData(object):
    MAX_LEVEL: int = 100
    MAX_MILEAGE: int = 10000
    MAX_GEAR: int = 5

    def __get_current_gas_level(self) -> int:
        return self.__current_gas_level

    def __set_current_gas_level(self, current_gas_level: int):
        self.__current_gas_level = current_gas_level

    def __get_current_gear(self) -> int:
        return self.__current_gear

    def __set_current_gear(self, current_gear: int):
        self.__current_gear = current_gear

    def __get_current_mileage(self) -> int:
        return self.__current_mileage

    def __set_current_mileage(self, current_mileage: int):
        self.__current_mileage = current_mileage

    def __get_oil_health(self) -> float:
        return self.__oil_health

    def __set_oil_health(self, oil_health: float):
        self.__oil_health = oil_health

    def __get_tires(self) -> array(Tire):
        return self.__tires

    def __set_tires(self, tires: array(Tire)):
        self.__tires = tires

    current_gear = property(__get_current_gear, __set_current_gear)
    current_gas_level = property(__get_current_gas_level, __get_current_gas_level)
    current_gas_mleage = property(__get_current_mileage, __set_current_mileage)
    oil_health = property(__get_oil_health, __set_oil_health)
    tires = property(__get_tires, __set_tires)