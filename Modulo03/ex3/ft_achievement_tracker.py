#! /usr/bin/python3


import random


def gen_player_achievements(achievements: set[str]) -> set[str]:
    count = random.randint(2, len(achievements))
    return set(random.sample(list(achievements), count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    achievements = {
                'Crafting Genius',
                'Strategist',
                'World Savior',
                'Speed Runner',
                'Survivor',
                'Master Explorer',
                'Treasure Hunter',
                'Unstoppable',
                'First Steps',
                'Collector Supreme',
                'Untouchable',
                'Sharp Mind',
                'Boss Slayer'
                }
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)
    print()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print()
    distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {distinct}")
    print()

    common = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements : {common}")
    print()

    different_alice = alice.difference(bob, charlie, dylan)
    print(f"Only Alices has: {different_alice}")
    different_bob = bob.difference(alice, charlie, dylan)
    print(f"Only Bob has: {different_bob}")
    different_charlie = charlie.difference(bob, alice, dylan)
    print(f"Only Charlie has: {different_charlie}")
    different_dylan = dylan.difference(bob, charlie, alice)
    print(f"Only Dylan has: {different_dylan}")
    print()

    print()
    missing_alice = set.difference(achievements, alice)
    print(f"Alice is missing: {missing_alice}")
    missing_bob = set.difference(achievements, bob)
    print(f"Bob is missing: {missing_bob}")
    missing_charlie = set.difference(achievements, charlie)
    print(f"Charlie is missing: {missing_charlie}")
    missing_dylan = set.difference(achievements, dylan)
    print(f"Dylan is missing: {missing_dylan}")


if __name__ == "__main__":
    main()
