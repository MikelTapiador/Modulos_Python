#! /usr/bin/python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    data = ["25", "abc", "100", "-50"]
    for d in data:
        try:
            print(f"Input data is '{d}'")
            temperature = input_temperature(d)
            print(f"temperature is now {temperature} ºC")
            print()
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
            print()
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
