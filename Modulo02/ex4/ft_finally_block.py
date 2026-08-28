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


def water_plant(plant_name):
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system():
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    data = ["Tomato", "Lettuce", "Carrots"]
    try:
        for d in data:
            water_plant(d)
    except PlantError as error:
        print(f"Caught PlantError {error}")
        print("..ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()

    print("Testing invalid plants...")
    print("Opening watering system")
    data = ["Tomato", "lettuce", "Carrots"]
    try:
        for d in data:
            water_plant(d)
    except PlantError as error:
        print(f"Caught PlantError {error}")
        print("..ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
