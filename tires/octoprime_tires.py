from tires.tires import Tires

class OctoPrimeTires(Tires):
    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        sum = 0
        for tire_wear in self.tires_wear:
            sum += tire_wear
        if sum >= 3:
            return True
        return False