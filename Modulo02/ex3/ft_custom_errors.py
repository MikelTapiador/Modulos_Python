#! /usr/bin/python3


class GardenError(Exception):
    def __init__(self, message: str = "Unkwon GardenError"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!"):
        super().__init__(message)


def check_plant(plant: bool) -> None:
    if plant is True:
        raise PlantError
    else:
        print("Plant is beautifull")


def check_tank(tank: bool) -> None:
    if tank:
        raise WaterError
    else:
        print("Tank is full")


def main():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        check_plant(True)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()
    print("Testing WaterError...")
    try:
        check_tank(True)
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant(True)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        check_tank(True)
    except Exception as error:
        print(f"Caught GardenError: {error}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
