#! /usr/bin/python3


import sys


def arguments() -> None:
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print("Total arguments: 1")
    else:
        print(f"Arguments received : {len(sys.argv) - 1}")
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i} : {sys.argv[i]}")
            i = i + 1
        print(f"Total arguments: {len(sys.argv)}")


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    arguments()


if __name__ == "__main__":
    main()
