class Plant:
    """
    Class representing a plant with basic attributes.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


"""ft_plant_factory.py - Plant Factory Module"""


def build_plants(data: list[tuple[str, int, int]]) -> list[Plant]:
    return [Plant(name, height, age) for name, height, age in data]


if __name__ == "__main__":
    plant_data = [
        ("Rose", 25, 30),
        ("Sunflower", 80, 45),
        ("Cactus", 120, 15),
        ("Tulip", 30, 20),
        ("Daisy", 15, 10)
    ]

    plants = build_plants(plant_data)

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", plant.get_info())
    print(f"\nTotal plants created: {len(plants)}")
