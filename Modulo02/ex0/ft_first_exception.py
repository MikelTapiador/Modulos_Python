#! /usr/bin/python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    data = ["25", "abc"]
    for d in data:
        try:
            print(f"Input data is '{d}'")
            temperature = input_temperature(d)
            print(f"temperature is now {temperature} ºC")
            print()
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
