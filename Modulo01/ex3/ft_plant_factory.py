#! /usr/bin/python3


class Plant:
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age(self) -> None:
        self.days = self.days + 1


def main() -> None:
    Plants = [Plant("Rose", 25.0, 30, 0.8),
              Plant("Oak", 200.0, 365, 1.5),
              Plant("Cactus", 5.0, 90, 2.0),
              Plant("Sunflower", 80.0, 45, 3.0),
              Plant("Fern", 15.0, 120, 4.5)]

    print("=== Plant Factory Output ===")

    for plant in Plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
