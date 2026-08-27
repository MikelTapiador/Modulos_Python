#! /usr/bin/python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float
            ) -> None:
        self._name = name
        self._height = height
        self._days = days
        self._growth_rate = growth_rate
        self._stats = self.Statistics()

    def show(self) -> None:
        print(
         f"{self._name}: {round((self._height), 1)}cm, {self._days} days old"
            )
        self._stats.record_show()

    def grow(self) -> None:
        self._height = self._height + self._growth_rate
        self._stats.record_grow()

    def age(self) -> None:
        self._days = self._days + 20
        self._stats.record_age()

    @staticmethod
    def is_older(days: int) -> bool:
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def anonymus(cls) -> "Plant":
        return cls("Unkwown plant", 0.0, 0, 0.0)


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            color: str,
            isbloomed: int,
            ) -> None:
        super().__init__(name, height, days, growth_rate)
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
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
                self,
                name: str,
                height: float,
                days: int,
                growth_rate: float,
                trunk_diameter: float,
                ) -> None:
        super().__init__(name, height, days, growth_rate)

        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and "
              f"{self.trunk_diameter}cm wide.")
        self._stats.record_shade()


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            color: str,
            isbloomed: int,
            seeds: int,
            ) -> None:
        super().__init__(name, height, days, growth_rate, color, isbloomed)
        self._seeds = seeds

    def show_seeds(self):
        print(f" Seeds: {self._seeds}")

    def grow(self):
        super().grow()
        self._seeds += 42


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> "
          f"{Plant.is_older(30)}")
    print("Is 400 days more than a year? -> "
          f"{Plant.is_older(400)}")
    print()

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, 8.0, "red", 0)
    flower.show()
    flower.ask()
    print("[statistics for Rose]")
    flower._stats.display()
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.show()
    flower.bloom()
    flower.ask()
    print("[statistics for Rose]")
    flower._stats.display()
    print()

    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 1.0, 5.0)
    tree.show()
    print("[statistics for Oak]")
    tree._stats.display()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("[statistics for Oak]")
    tree._stats.display()
    print()

    print("=== Seed")
    seed = Seed("Sunflower", 80.0, 45, 30.0, "yellow", 0, 0)
    seed.show()
    seed.ask()
    seed.show_seeds()
    print("[make sunflower grow, age and bloom]")
    seed.grow()
    seed.age()
    seed.show()
    seed.bloom()
    seed.ask()
    seed.show_seeds()
    print("[statistics for Sunflower]")
    seed._stats.display()
    print()

    print("=== Anonymous")
    unkwown = Plant.anonymus()
    unkwown.show()
    print("[statistics for Unknown plant]")
    unkwown._stats.display()


if __name__ == "__main__":
    main()
