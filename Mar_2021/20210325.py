"""
1603. Design Parking System

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

"""
#SOLUTION 1
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.dict_parking_lot = {
        1 : big,
        2 : medium,
        3 : small
        }

    def addCar(self, carType: int) -> bool:
        if self.dict_parking_lot[carType]>0:
            self.dict_parking_lot[carType] -= 1
            return True
        else:
            return False

#SOLUTION 2
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.vacancy_b = big
        self.vacancy_m = medium
        self.vacancy_s = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.vacancy_b > 0:
                self.vacancy_b -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.vacancy_m > 0:
                self.vacancy_m -= 1
                return True
            else:
                return False
        if carType == 3:
            if self.vacancy_s > 0:
                self.vacancy_s -= 1
                return True
            else:
                return False