import random

tests = {(11,15,17,20,21,21,21,21,23,25,26,27,28,29) : 21, () : 1, (11,11,15,15,15,15,21,25,35,45) : 21, () : 5}

def generate_list ():
    no_of_elements = random.randint(11,31)
    generated_list = []
    while  len(generated_list) < no_of_elements :
        generated_list.append(random.randint(1,1001))
    generated_list.sort()
    return generated_list

def game_start(stepwise_print = True) :
    sorted_list = generate_list()
    random_number = random.choice(sorted_list)
    if stepwise_print == True :
        print(f"random number is {random_number}")
        print(f"no. of elements in list are  {len(sorted_list)}")
    return (sorted_list, random_number)

def chose_number_bot_game (sorted_list, random_number) :
    # sorted_list, random_number = game_start(False)
    # sorted_list, random_number = [11,15,17,20,21,21,21,21,23,25,26,27,28,29], 21

        used_places = []
        lower_limit = 0
        upper_limit = len(sorted_list) 
        i = 0
        while len(used_places) < len(sorted_list):
            if i == 0 :
                chosen_place = len(sorted_list)//2
            else :
                if no_on_guessed_spot < random_number :
                    lower_limit = chosen_place
                    chosen_place = (upper_limit+chosen_place)//2
                if no_on_guessed_spot > random_number :
                    upper_limit = chosen_place
                    chosen_place = (lower_limit+chosen_place)//2


            used_places.append(chosen_place)
            if sorted_list[chosen_place] == random_number :
                a = 1
                while chosen_place - a >= 0 and sorted_list[chosen_place-a] == random_number  :
                    chosen_place = chosen_place - a
                    a += 1
                return ("w",chosen_place + 1, i+1)
            elif sorted_list[chosen_place] != random_number :
                no_on_guessed_spot = (sorted_list[chosen_place])
            i += 1
        return(-1)
        # if sorted_list[chosen_place] != random_number :
        #     return ("l", sorted_list, random_number, i+1)

# print(chose_number_bot_game())

def chose_number_bot_game_tests() :
    for keys, values in tests.items() :
        run_test = chose_number_bot_game(list(keys), values)
        print(run_test)
    
# chose_number_bot_game_tests()

if __name__ == "__main__":
    tests = [
        ([11,15,17,20,21,21,21,21,23,25,26,27,28,29], 21),
        ([], 1),
        ([11,11,15,15,15,15,21,25,35,45], 21),
        ([], 5),
        ([10],5)
    ]

    for lst, target  in tests:
        print(chose_number_bot_game(lst, target))
