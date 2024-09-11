"""This program is to help plan a tea party and have 
the right amount of tea bags and treats per number of guests
"""

__author__: str = "730467763"


def main_planner(guests: int) -> None:
    """calls all the functions"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")
    # print the results on the screen


def tea_bags(people: int) -> int:
    """calculates the number of people attending the party and how
    many bags of tea is needed"""
    return people * 2


# shows that each guest needs two bags#


def treats(people: int) -> int:
    """calculates the number of people attending and how
    many treats they need"""
    return int(tea_bags(people=people) * 1.5)


# shows that each guest needs 1.5 treats#


def cost(tea_count: int, treat_count: int) -> float:
    """this calcualtes the total cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


# shows each tea bag cost 50 cents and each treat cost 75 cents#


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
