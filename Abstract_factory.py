from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def has_legs(self):
        pass

class ModernChair(Chair):
    def has_legs(self):
        return "Modern chair with legs"

class VictorianChair(Chair):
    def has_legs(self):
        return "Victorian chair with legs"

class Sofa(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class ModernSofa(Sofa):
    def sit_on(self):
        return "Sitting on a modern sofa"

class VictorianSofa(Sofa):
    def sit_on(self):
        return "Sitting on a Victorian sofa"

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()

# Usage
def get_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    return chair.has_legs(), sofa.sit_on()

print(get_furniture(ModernFurnitureFactory()))
print(get_furniture(VictorianFurnitureFactory()))
