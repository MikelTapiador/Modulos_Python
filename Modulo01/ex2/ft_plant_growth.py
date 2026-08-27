#! /usr/bin/python3

class Plant:
    name: str
    height: float
    days: int

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.days = self.days + 1


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30

    initial_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()

    weekly_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {weekly_growth}cm")


if __name__ == "__main__":
    main()
