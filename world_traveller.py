# World Traveller
# Author: Aishani
# Date: Nov 3 2023

# greet user
name = input("What's your name? ")

print(f"{name.capitalize()}! Nice to meet you! ")

tally_continent = 0

continents = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antartica"]

for continent in continents:
    continent_arrival = input(f"Have you been to {continent}? ")
    if continent_arrival.lower().strip(".,!? ") == ("yes"):
        tally_continent = tally_continent + 1
    elif continent_arrival.lower().strip(",.!? ") == ("no"):
        tally_continent = tally_continent
    else:
        break

print(f"I see, you've visited {tally_continent} / 7 continents!")