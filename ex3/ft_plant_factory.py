class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


def build_plants(data):
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
    print(f"Total plants created: {len(plants)}")
