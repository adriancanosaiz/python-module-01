class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self):
        self.height += 1
    def advance_age(self):
        self.age += 1
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 120, 15)

    plants = [rose, sunflower, cactus]
    initial_heights = {plant.name: plant.height for plant in plants}

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for day in range (6):
        for plant in plants:
            plant.grow()
            plant.advance_age()

    print("\n=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        growth = plant.height - initial_heights[plant.name]
        print(f"Growth this week: +{growth}cm.\n")