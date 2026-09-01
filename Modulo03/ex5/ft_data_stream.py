#! /usr/bin/python3

import typing

import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    list_name = [
            "Alice",
            "Bob",
            "Charlie",
            "Dylan"
        ]
    action_name = [
            "run",
            "eat",
            "sleep",
            "grab",
            "move",
            "climb",
            "swim",
            "use",
            "release"
        ]
    while True:
        yield random.choice(list_name), random.choice(action_name)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        random_event = random.choice(events)
        events.remove(random_event)
        yield random_event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for event_number in range(1000):
        player, action = next(stream)
        print(
            f"Event {event_number}: Player {player} did action {action}"
        )

    events: list[tuple[str, str]] = []

    for _ in range(10):
        game_event = next(stream)
        events.append(game_event)

    print(f"Built list of 10 events: {events}")

    for game_event in consume_event(events):
        print(f"Got event from list: {game_event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
