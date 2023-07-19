# Python program for the execution of hat covered cats search algorithm
# The function will outputs which cats have hats at the end
# Defining the function

# 1) Create a list of given number of cats, initially with no hats.
# 2) Iterate from round 1 to given round number:
#   a. For each round, iterate through the cats.
#   b. For each cat, check if the cats position is divisible by the current round number without remainder.
#   If it is, toggle the hat (put it on if it does not have one, or take it off if it does).
# 3) After the given number of rounds, output the positions of the cats that have hats.

def calculate_hats(num_cats: int, num_rounds: int) -> list:
    cats_list = [False] * num_cats
    for round in range(1, num_rounds+1):
        for i, cat in enumerate(cats_list):
            if i % round == 0:
                cats_list[i] = not cat
    cats_position = [i for i, cat in enumerate(cats_list) if cat]
    return cats_position


print(calculate_hats(100, 100))

# Complexity of this operation:
# 1) We need to interate trought each round O(n)
# 2) We need to interate trought each cat O(n)
# Result -> O(n^2)
