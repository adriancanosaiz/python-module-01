class Plant:
    """Base class for all plants."""
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.growth = 0

    def grow(self):
        self.height += 1
        self.growth += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that can bloom and has a color."""
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Special rare flower that has Prize Points."""
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class Garden:
    """Represents a garden belonging to a person."""

    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def grow_all(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")

        types = GardenManager.Stats.count_types(self.plants)

        print(f"\nPlants added: {len(self.plants)}, "
              f"Total growth: {GardenManager.Stats.total_growth(self.plants)}"
              f"cm")
        print(
            f"Plant types: {types['regular']} regular, "
            f"{types['flowering']} flowering, "
            f"{types['prize']} prize flowers"
        )


class GardenManager:
    gardens_managed = 0

    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)
        GardenManager.gardens_managed += 1

    @classmethod
    def create_garden_network(cls):
        gm = cls()

        alice = Garden("Alice")
        bob = Garden("Bob")

        oak = Plant("Oak Tree", 100)
        alice.add_plant(oak)
        print(f"Added {oak.name} to Alice's garden")

        rose = FloweringPlant("Rose", 25, "red")
        alice.add_plant(rose)
        print(f"Added {rose.name} to Alice's garden")

        sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
        alice.add_plant(sunflower)
        print(f"Added {sunflower.name} to Alice's garden")

        bob.add_plant(PrizeFlower("Orchid", 30, "purple", 20))
        bob.add_plant(FloweringPlant("Daisy", 15, "white"))
        bob.add_plant(Plant("Cactus", 40))

        gm.add_garden(alice)
        gm.add_garden(bob)

        return gm

    class Stats:

        @staticmethod
        def total_growth(plants):
            return sum(p.growth for p in plants)

        @staticmethod
        def height_validation(plant, limit):
            return plant.height > limit

        @staticmethod
        def count_types(plants):
            regular = sum(isinstance(p, Plant) and not
                          isinstance(p, (FloweringPlant, PrizeFlower))
                          for p in plants)
            flowering = sum(isinstance(p, FloweringPlant) and not
                            isinstance(p, PrizeFlower)
                            for p in plants)
            prize = sum(isinstance(p, PrizeFlower) for p in plants)
            return {"regular": regular, "flowering": flowering, "prize": prize}

        @classmethod
        def calculate_garden_score(cls, garden):
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            score += cls.total_growth(garden.plants)
            return score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    alice = manager.gardens[0]
    bob = manager.gardens[1]

    alice.grow_all()

    alice.report()

    test_plant = Plant("Test Plant", 120)
    print("\nHeight validation test:",
          GardenManager.Stats.height_validation(test_plant, 100))

    print(f"Garden scores - Alice: "
          f"{GardenManager.Stats.calculate_garden_score(alice)}, "
          f"Bob: {GardenManager.Stats.calculate_garden_score(bob)}")

    print(f"Total gardens managed: {GardenManager.gardens_managed}")
