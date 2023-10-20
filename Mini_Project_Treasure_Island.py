print(f"Welcome to the Treasure island. \nYour mission is to find the treasure")
direction = input("Select direction : left or right ? : ")
lower_direction = direction.lower()
if direction == "right":
    option = input("Select any, You have two options for going island swim or wait for the boat? : ")
    if option == "wait":
        doors = input("now you are here in house. select any door, you have three doors red, blue, green ? : ")
        if doors == "red":
            print("Opps!! Burned by fire Game Over....!!!!")
        elif doors == "blue":
            print("Opps!! Eaten by beast Game Over....!!!!")
        else:
            print("Winner Winner Chicken Dinner!!!!")
    else:
        print("Opps!! Attack by trout Game Over....!!!!")
else:
    print("Opps!! Fall into a hole Game Over....!!!!")

