import random
import time

# l = [5,7,9,11,2,50,60, 101]
def addlist(l):
    for i in range (len(l)-1) :
        a = l[0] + l[1]
        l.pop(0)
        l[0] = a
    return a
# print(addlist(l))


def guessnum() :
    z = random.randint(1,100)
    print("Game Start")
    print("Number is from 1 to 100(including both)".title())
    print("You Have Ten Guesses\n")
    i = 0
    t1 = time.perf_counter()
    while i < 11 :
        i += 1
        a = int(input(f"Guess Number {i} : "))

        if 0 < a < z :
            print("Number is Larger")
        elif 101 > a > z :
            print("Number is Smaller")
        elif a == z :
            print("You Won")
            print(f"you took {i} guesses to win".title())
            t2 = time.perf_counter()
            print(f"you took {t2-t1} seconds".title())
            break
        else :
            print("Can't You See Number Is Between 0 and 101")
            i -= 1
    if a != z : print("Your all guesses are over, you lose".title())

# guessnum()


def guessnums():
    b = input("want to play guessing game (yes or no): ".title())
    while b == "yes" :
        guessnum()

    print("ok then, bye".title())

# guessnums()

def guessing_bot() :
        z = random.randint(1,100)
        print("Game Start")
        f = 0
        l = 100
        print(f"Number is from {f+1} to {l}(including both)".title())
        print("You Have Ten Guesses\n")
        i = 1
        c = 0
        t1 = time.perf_counter()
        a = 50
        b = int(a)
        y = [0, a]
        z = 100
        print(z)
        while i < 11 :
            i += 1

            print(f"your guess :{b}".title())
            if 0 < b < z :
                print("Number is Larger")
                # a = (a + (l-a)//2) # if isinstance((l-a)/2, int) is True else ((l-a-1)/2)
                a = (a + (y[0]+y[1])/2) if i == 2 else (a+((y[i-1]-y[i-2])/2))+1 if a == (a+((y[i-1]-y[i-2])//2)) else (a+((y[i-1]-y[i-2])/2)) if (y[i-1]-y[i-2])/2 > (y[i-2]-y[i-1])/2 else (a+((y[i-2]-y[i-1])/2))
                print(a)
                b = int(a)
                # time.sleep(2)
            elif 101 > b > z :
                print("Number is Smaller")
                # a = (a-(f+a)//2) # if isinstance((f+a)/2, int) is True else ((f+a+1)/2)
                a = (a - (y[0]+y[1])/2) if i == 2 else (a-((y[i-1]-y[i-2])/2)) if (y[i-1]-y[i-2])/2 > (y[i-2]-y[i-1])/2 else (a-((y[i-2]-y[i-1])/2))
                b = int(a)
                # time.sleep(2)
            elif b == z :
                print("You Won")
                print(f"you took {i} guesses to win".title())
                t2 = time.perf_counter()
                print(f"you took {t2-t1} seconds".title())
                break
            else :
                print("Can't You See Number Is Between 0 and 101")
                i -= 1
                time.sleep(4)
            y.append(a)
        if b != z : print("Your all guesses are over, you lose".title())
        if b != z : c +=1
        return[z, i, c]
# print(guessing_bot())
guessing_bot()
# print(75+(25/2))

# print(isinstance(5.5, int))

def auto_guesses (e):
    i = 0
    l = []
    m = []
    nl = []

    while i < e :
        p = guessing_bot()
        l.append(p[0])
        m.append(p[1])
        nl.append(p[2])
        i += 1
    print("random numbers", l)
    print("moves taken", m)
    print(f"average moves takes : {(addlist(m))/e}")
    # print("win or loss", nl)
    print(f"number of losses {addlist(nl)}")
# auto_guesses(100001)


class guess_bots:
    def guessing_bot() :
        z = random.randint(1,100)
        print("Game Start")
        f = 0
        l = 100
        print(f"Number is from {f+1} to {l}(including both)".title())
        print("You Have Ten Guesses\n")
        i = 1
        c = 0
        t1 = time.perf_counter()
        a = 50
        b = int(a)
        y = [0, a]
        # z = 100
        print(z)
        while i < 11 :
            i += 1

            print(f"your guess :{b}".title())
            if 0 < b < z :
                print("Number is Larger")
                # a = (a + (l-a)//2) # if isinstance((l-a)/2, int) is True else ((l-a-1)/2)
                a = (a + (y[0]+y[1])/2) if i == 2 else (a+((y[i-1]-y[i-2])/2)) if (y[i-1]-y[i-2])/2 > (y[i-2]-y[i-1])/2 else (a+((y[i-2]-y[i-1])/2))
                b = int(a)
                # time.sleep(2)
            elif 101 > b > z :
                print("Number is Smaller")
                # a = (a-(f+a)//2) # if isinstance((f+a)/2, int) is True else ((f+a+1)/2)
                a = (a - (y[0]+y[1])/2) if i == 2 else (a-((y[i-1]-y[i-2])/2)) if (y[i-1]-y[i-2])/2 > (y[i-2]-y[i-1])/2 else (a-((y[i-2]-y[i-1])/2))
                b = int(a)
                # time.sleep(2)
            elif b == z :
                print("You Won")
                print(f"you took {i} guesses to win".title())
                t2 = time.perf_counter()
                print(f"you took {t2-t1} seconds".title())
                break
            else :
                print("Can't You See Number Is Between 0 and 101")
                i -= 1
                time.sleep(4)
            y.append(a)
        if b != z : print("Your all guesses are over, you lose".title())
        if b != z : c +=1


    # guessing_bot()
    # print(isinstance(5.5, int))

    def auto_guesses (e):
        i = 0
        l = []
        m = []
        nl = []

        while i < e :
            p = guess_bots.guessing_bot()
            l.append(p.a.z)
            m.append(p.a.i)
            nl.append(p.a.c)

            i += 1
        # print("random numbers", l)
        # print("moves taken", m)
        # print("win or loss", l)


# auto_guesses(2)
def function_a():
    my_variable = "Hello"
    function_b(my_variable)
def function_b(data):
    print(data)
# function_a()