# Similarity Score Input
# Author: Aishani
# Date: Nov 17 2023

print("Please enter hobbies, separated by spaces: ")
person_1_hobbies = input("Person 1: ")
person_2_hobbies = input("Person 2: ")

person_1_hobbies_list = (person_1_hobbies).strip(".,?! ").lower().split()
person_2_hobbies_list = (person_2_hobbies).strip(".,?! ").lower().split()

sim_score = 0

for hobby in person_1_hobbies_list:
    if hobby in person_2_hobbies_list:
        sim_score += 1
    else:
        sim_score = sim_score

print(f"You have {sim_score} hobbies in common!")