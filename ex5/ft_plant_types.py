class Plant:
    """
    Class representing a plant with basic attributes.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        plant_type = self.__class__.__name__
        return f"{self.name} ({plant_type}): {self.height}cm, {self.age} days"


class Flower(Plant):
    """
    Class representing a flower, inheriting from Plant.
    """
    def __init__(self, name: str,
                 height: int,
                 age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, {self.color.lower()} color"


class Tree(Plant):
    """
    Class representing a tree, inheriting from Plant.
    """
    def __init__(self, name: str,
                 height: int,
                 age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        shade = self.trunk_diameter * 2
        return f"{self.name} provides {shade:.0f} square meters of shade."

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """
    Class representing a vegetable, inheriting from Plant.
    """
    def __init__(self, name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self) -> str:
        return f"The {self.name} is rich in {self.nutritional_value}."

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, {self.harvest_season.lower()} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "Red")
    tulip = Flower("Tulip", 30, 20, "Yellow")

    oak = Tree("Oak", 500, 100, 1.5)
    pine = Tree("Pine", 600, 80, 1.2)

    carrot = Vegetable("Carrot", 30, 60, "Fall", "Vitamin A")
    tomato = Vegetable("Tomato", 50, 80, "Summer", "Vitamin C")

    plants = [rose, tulip, oak, pine, carrot, tomato]
    for plant in plants:
        print(plant.get_info())
        if isinstance(plant, Flower):
            print(plant.bloom())
        elif isinstance(plant, Tree):
            print(plant.produce_shade())
        elif isinstance(plant, Vegetable):
            print(plant.harvest())
        print()
