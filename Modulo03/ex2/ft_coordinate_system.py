#! /usr/bin/python3


import math


class CoordinatSyntaxError(ValueError):
    pass


def get_player_pos() -> tuple[float, float, float]:
    while True:
        data = input("Enter new coordinates as floats in format 'x,y,z': ")
        raw_coordinates = data.split(",")

        try:
            if len(raw_coordinates) != 3:
                raise ValueError("Invalid syntax")

            coordinates: list[float] = []
            for coordinate in raw_coordinates:
                try:
                    coordinates.append(float(coordinate))
                except ValueError as error:
                    print(f"Error on parameter '{coordinate}': {error}")
                    raise ValueError

            return (coordinates[0], coordinates[1], coordinates[2])
        except ValueError:
            if len(raw_coordinates) != 3:
                print("Invalid syntax")


def distance(
        x1: float, y1: float, z1: float, x2: float, y2: float, z2: float
        ) -> float:
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(result, 4)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    data = get_player_pos()
    print(f"Got a first tuple: {data}")
    x1 = data[0]
    y1 = data[1]
    z1 = data[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_between = distance(0.0, 0.0, 0.0, x1, y1, z1)
    print(f"Distance to center: {distance_between}")
    print()

    print("Get a second set of coordinates")
    data = get_player_pos()
    x2 = data[0]
    y2 = data[1]
    z2 = data[2]
    distance_between = distance(x1, y1, z1, x2, y2, z2)
    print(f"Distance between the 2 sets of coordinates: {distance_between}")


if __name__ == "__main__":
    main()
