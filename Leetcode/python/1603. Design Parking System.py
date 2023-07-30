class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots=[big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType==0:
            return None
        if self.slots[carType-1]>0:
             self.slots[carType-1]-=1
             return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
out = []
out.append(obj.addCar(1))
out.append(obj.addCar(1))
out.append(obj.addCar(0))
print(out)