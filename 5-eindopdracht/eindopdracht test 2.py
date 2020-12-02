from time import sleep

def telop():

    count = input("tot hoeveel seconden wil je tellen")
    x = int()
    for x in range (1, count+1):
        print(x, "seconden voorbij")
        sleep(1)

    print("test")