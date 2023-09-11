from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for a in self.tire_wear:
            if a >= 3.0:
                return True
        return False