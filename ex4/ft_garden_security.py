"""Module for secure plant data management."""


class SecurePlant:
    """Class representing a plant with secure attributes."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the SecurePlant with name, height, and age.
        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.__height = height
        self.__age = age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self) -> str:
        return (
            f"Current plant: {self.name} ("
            f"{self.__height}cm, {self.__age} days)"
        )


if __name__ == "__main__":
    plant = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(plant.get_info())

    plant.set_height(45)
    plant.set_age(25)
    print(plant.get_info())

    print("")

    plant.set_height(-10)
    plant.set_age(-5)
    print(plant.get_info())
