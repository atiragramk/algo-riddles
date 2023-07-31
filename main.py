import math
from cProfile import Profile
from pstats import SortKey, Stats
# Python program for the execution of hat covered cats search algorithm
# The function will outputs which cats have hats at the end
# Defining the function

# 1) Create a list of given number of cats, initially with no hats.
# 2) Iterate from round 1 to given round number:
#   a. For each round, iterate through the cats.
#   b. For each cat, check if the cats position is divisible by the current round number without remainder.
#   If it is, toggle the hat (put it on if it does not have one, or take it off if it does).
# 3) After the given number of rounds, output the positions of the cats that have hats.
# OR
# 1) Create a list of given number of cats, initially with no hats.
# 2) Iterate through the cats:
#   a. Check if the square of cat position index is integer and it's still not above quantity of rounds
#   b. If previous statement is True put hat on the cat
# 3) Output the positions of the cats that have hats.

ROUNDS = 10000
CATS_NUMBER = ROUNDS
CATS_HATS = [False] * CATS_NUMBER


def main(variant) -> None:
    if variant:
        for round in range(1, ROUNDS+1):
            for i, cat in enumerate(CATS_HATS):
                if i % round == 0:
                    CATS_HATS[i] = not cat
        print([i for i, cat in enumerate(CATS_HATS) if cat])
        return
    # Complexity of this operation:
    # 1) We need to interate trought each round O(n)
    # 2) We need to interate trought each cat O(m)
    # Result -> O(n*m)
    for i, cat in enumerate(CATS_HATS):
        if i and math.sqrt(i).is_integer() and i < ROUNDS:
            CATS_HATS[i] = not cat
    print([i for i, cat in enumerate(CATS_HATS) if cat])
    # Complexity of this operation:
    # 1) We need to interate trought each cat O(n)
    # Result -> O(n)


if __name__ == "__main__":
    with Profile() as profile:
        main(1)  # 0 or 1
        Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()
