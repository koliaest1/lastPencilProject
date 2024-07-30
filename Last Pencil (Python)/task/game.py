import random

pencil = "|"
names = ["John", "Jack"]


# Function to switch players
def next_player(user_name):
    return "Jack" if user_name == "John" else "John"


# Function to handle a user's turn
def user_turn(user_name, count):
    while True:
        print(f"{user_name}'s turn!")
        remove = input()
        if remove.isdigit() and int(remove) in range(1, 4):
            if int(remove) > count:
                print("Too many pencils were taken")
            else:
                count -= int(remove)
                if count > 0:
                    print(pencil * count)
                return count, next_player(user_name)
        else:
            print("Possible values: '1', '2' or '3'")


def bot_turn(user_name, count):
    print(f"{user_name}'s turn:")
    while True:
        if count == 1:
            remove = 1
        elif count % 4 == 2:
            remove = 1
        elif count % 4 == 3:
            remove = 2
        elif count % 4 == 0:
            remove = 3
        elif count % 4 == 1:
            remove = random.randint(1, 3)
        print(remove)
        count -= remove
        print(pencil * count)
        return count, next_player(user_name)


while True:
    print("How many pencils would you like to use: ")
    number_of_pencils = input()
    if number_of_pencils.isdigit():
        number_of_pencils = int(number_of_pencils)
        if number_of_pencils > 0:
            pencils_count = number_of_pencils
            while True:
                print(f"Who will be the first ({names[0]}, {names[1]})")
                name = input()
                if name in names:
                    print(pencil * int(number_of_pencils))
                    while pencils_count > 0:
                        if name == "John":
                            pencils_count, name = user_turn("John", pencils_count)
                        elif name == "Jack":
                            pencils_count, name = bot_turn("Jack", pencils_count)
                        if pencils_count == 0:
                            print(f'{name} won!')
                            exit()
                else:
                    print("Choose between John and Jack")
        else:
            print("The number of pencils should be positive")
    else:
        print("The number of pencils should be numeric")
