class Car:
    def __init__(self):
        self.color = ''
        self.fuel = 0
        self.brand = ''
        self.year = 0

    def go(self):
        print("Автомобиль поехал.")

    def turn(self):
        print("Автомобиль повернул.")

    def stop(self):
        print("Автомобиль остановился.")

    def info(self):
        print(f"Информация об автомобиле:")
        print(f"Марка: {self.brand}")
        print(f"Скорость: {self.speed}")
        print(f"Цвет: {self.color}")
        print(f"Уровень топлива: {self.fuel}")

myCar = Car()
myCar.color = 'blue'
myCar.fuel = 50
myCar.brand = 'BMW'
myCar.speed = 333

myCar.info()