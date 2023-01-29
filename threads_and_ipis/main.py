from threading import Thread
from time import sleep


def car_one(speed):
    """ example with cars, let's say where it will start """
    path_car = 0
    while path_car <= 100:
        path_car += speed
        sleep(0.5)
        print("First car: ", path_car)


def car_two(speed):
    """ same function with the second car """
    path_car = 0
    while path_car <= 100:
        path_car += speed
        sleep(0.5)
        print("Second car: ", path_car)


thread_car_one = Thread(target=car_one, args=[1])
thread_car_two = Thread(target=car_two, args=[1.5])

thread_car_one.start()
thread_car_two.start()
