# AOC Day 1
# Author: Aishani
# 30 November 2023

# There is one elf carrying the most calories
# How many does that one have

# Create a list that holds all the calories of the elves 

# Open the file
with open("./aoc2022day1.txt") as f:
    # Calories of current elf
    current_cals = 0

    for line in f:
        # If there is something in the line
        if line.strip():
                current_cals += int(line.strip())

print(current_cals)