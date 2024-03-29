# Winter Holidays Review
# Author: Aishani
# 8 January 2024

# Requirements:
#  - create a function called winter_holiday()
#  - take one parameter
#      - string
#  - return a summary of an event from your holidays

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - indicate what kind of event to summarize

    Returns:
        an event that happened during the holidays
        the event is selected randomly"""
    
    # Create a list of good and bad events
    good_list = [
    "I went to Nepal and spent time with my family.",
    "I saw Mount Everest!",
    "I got to experience many new things.",
    "I ate instant noodles everyday for a week straight!"
]

    bad_list = [
    "A cat died :(",
    "I got really sick.",
    "The roof fell.",
    "One way travel was over 26 hours long!"
]

    # If the event is good, return a good event
    # TODO: return a randomly chosen good event 
    if good_or_bad.strip().lower() == "good":
        return random.choice(good_list)
    elif good_or_bad.strip().lower() == "bad":
        return random.choice(bad_list)
    else:
        print("Sorry, I only take good or bad events.")


def main() -> None:
    print(winter_holiday("good"))

    print(winter_holiday("bad"))

if __name__ == "__main__":
    main()