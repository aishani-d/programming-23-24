# Bubble Tea Popularity Algorithm
# Author: Aishani
# Date: 27 Oct 2023

# Ask 5 users what thier favourite bubble tea place is 
# Print out a summary of the data

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bbqueen_likes = 0

NUM_RESPONDENTS = 5

for _ in range(NUM_RESPONDENTS):

    # Ask the user what their favourtie bbt place is 
    print("What's your favourite bubble tea place? ")
    fave_bbt = input().strip(",.?!").lower()
    # Tallying/Coutnting Algo

    # Options: Coco, Chatime, SunTea, Xing Fu Tang, Bubble Queen
    # If they say coco increase the counter for coco by one, each time 

    if fave_bbt == "coco":
        coco_likes = coco_likes + 1
    elif fave_bbt == "chatime":
        chatime_likes += 1
    elif fave_bbt == "suntea":
        suntea_likes += 1
    elif fave_bbt == "xing fu tang":
        xingfutang_likes += 1
    elif fave_bbt == "bubble queen":
        bbqueen_likes += 1
    else:
        print(f"Sorry, I don't know {fave_bbt}.")

# Print out a summary of the results 
print(f"CoCo Likes: {coco_likes} | {}")
print(f"Chatime Likes: {chatime_likes}")
print(f"Suntea Likes: {suntea_likes}")
print(f"Xing Fu Tang Likes: {xingfutang_likes}")
print(f"Bubble Queen Likes: {bbqueen_likes}")

print()