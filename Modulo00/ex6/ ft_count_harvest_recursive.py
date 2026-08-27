
def ft_print_harvest(day, days):
    if day > days:
        print("Harvest time!")
        return

    print(f"Day {day}")

    ft_print_harvest(day + 1, days)


def ft_count_harvest_recursive():

    days = int(input("Enter days until harvest: "))
    ft_print_harvest(1, days)
