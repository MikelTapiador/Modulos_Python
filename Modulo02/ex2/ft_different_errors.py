#! /usr/bin/python3


def garden_operations(operation_number: int) -> float:
    value = 1.0
    if operation_number == 0:
        value = int("abc")
    elif operation_number == 1:
        value = 1/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        value = "abc" + 1
    elif operation_number == 4:
        value = 2.0 + 2.0
    return value


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for operation_number in range(0, 5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError:{error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
