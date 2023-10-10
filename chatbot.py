# Chatbot
# Author: Ubial
# Date: 21 September 2023

import random
import time 

# Greet the user
print("Hello there! 🤖")
print("I'm a crude chatbot, here to talk to you.")
time.sleep(1.5)

# Get the user's name and store it in a variable
user_name = input("So... what's your name? ")

# Respond with the user's name
time.sleep(1)
print(f"It's nice to meet you, {user_name}!")

# Ask the user what their favourite food is
fave_food = input(f"{user_name}, what's your favourite food? ")

# If they answer pasta, respond with something related
if fave_food == "pasta":
    print("🍝")
    print("I think I love pasta, too!")
elif fave_food == "burgers" or fave_food == "Burgers":
    print("🍔")
    print("Mmmmmm. Burgers!")
elif fave_food == "pizza" or fave_food == "Pizza":
    print("🍕")
    print("Pizza is the best.")
else:
    # Respond with something that is NOT TOO repetitive but appropriate
    # Create a list of appropriate responses
    list_of_fave_food_responses = [
        f"{fave_food}? I LOVE THAT!",
        "So delicious",
        "Interesting, I've never tried that before."
    ]
    time.sleep (1)
    # Printing a specific response
    # print(list_of_fave_food_responses[2])

    # Choose one response randomly from the list
    random_response = random.choice(list_of_fave_food_responses)

    # Print out the chosen response
    print(random_response)