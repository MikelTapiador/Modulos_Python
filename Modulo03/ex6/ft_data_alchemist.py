#! /usr/bin/python3


import random


def random_number() -> int:
    result = random.randint(0, 1000)
    return result


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()

    intial_list = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
        ]
    print(f"Initial list of players  {intial_list}")
    new_list = [name.capitalize() for name in intial_list]
    print(f"New list with all names capitalized: {new_list}")
    cap_list = [name for name in intial_list if name == name.capitalize()]
    print(f"New list of capitalized names only:{cap_list}")
    print()

    dictionary = {name: random_number() for name in new_list}
    print(f"Score dict: {dictionary}")
    average = round((sum(dictionary.values())) / (len(dictionary.values())), 2)
    print(f"Score average is {average}")
    high_dictionary = {
        person: number for person, number in dictionary.items()
        if number > average
        }
    print(f"High scores: {high_dictionary}")


if __name__ == "__main__":
    main()
