from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            sleep(1)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
            if self.enemies == 0:
                print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
