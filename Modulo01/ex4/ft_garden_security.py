#! /usr/bin/python3


class Plant:
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

    def show(self) -> None:
        print(f"{self._name}: {(self._height)}cm, {self._days} days old")

    def grow(self) -> None:
        self._height = self._height + self._growth_rate

    def age(self) -> None:
        self._days = self._days + 1

    def set_height(self, height) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can´t be negative")
            print("Height update rejected")
            return False
        self._height = height
        print(f"Height updated: {int(self._height)} cm")
        return True

    def set_age(self, days) -> bool:
        if days < 0:
            print(f"{self._name}: Error, age can´t be negative")
            print("Age update rejected")
            return False
        self._days = days
        print(f"Age updated: {self._days} days")
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days


def main() -> None:
    rose = Plant("Rose", 15.0, 10, 0.5)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-25.0)
    rose.set_age(-30)
    print()
    print(f"Current state: {rose._height}cm, {rose._days} days old")


if __name__ == "__main__":
    main()
