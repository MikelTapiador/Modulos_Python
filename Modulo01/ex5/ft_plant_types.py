#! /usr/bin/python3


class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            ) -> None:
        self._name = name
        self._height = height
        self._days = days

    def show(self) -> None:
        print(
         f"{self._name}: {round((self._height), 1)}cm, {self._days} days old"
            )


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str,
            isbloomed: int,
            ) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._isbloomed = isbloomed

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

    def bloom(self) -> None:
        if self._isbloomed == 0:
            self._isbloomed = 1
        else:
            print(f" {self._name} has already bloomed")

    def ask(self) -> None:
        if self._isbloomed == 0:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                days: int,
                trunk_diameter: float,
                ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and "
              f"{self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                days: int,
                harvest_season: str,
                nutritional_value: int
                ) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        self._height = self._height + 2.1
        self.nutritional_value = self.nutritional_value + 1

    def age(self) -> None:
        self._days = self._days + 1


def main():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red", 0)
    flower.show()
    flower.ask()
    print("[asking the rose to bloom]")
    flower.show()
    flower.bloom()
    flower.ask()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(1, 21):
        vegetable.age()
        vegetable.grow()
    vegetable.show()


if __name__ == "__main__":
    main()
