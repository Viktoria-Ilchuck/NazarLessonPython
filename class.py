class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.fuel = 100
        self.mileage = 0
        self.is_running = False

    def start(self):

        if self.fuel > 0:
            if not self.is_running:
                self.is_running = True
                print(f"{self.brand} {self.model} запущено.")
            else:
                print(f"{self.brand} {self.model} вже працює.")
        else:
            print(f"{self.brand} {self.model}: немає пального, спочатку заправте авто.")

    def stop(self):

        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} зупинено.")
        else:
            print(f"{self.brand} {self.model} вже вимкнено.")

    def drive(self, distance):
        if not self.is_running:
            print(f"{self.brand} {self.model}: двигун не запущений!")
            return

        fuel_needed = distance * 0.3

        if self.fuel >= fuel_needed:
            self.mileage += distance
            self.fuel -= fuel_needed
            print(f"{self.brand} {self.model} проїхав {distance} км. Залишок пального: {self.fuel} л.")
        else:
            print(f"{self.brand} {self.model}: недостатньо пального для поїздки.")

    def refuel(self, amount):

        if amount > 0:
            self.fuel += amount
            if self.fuel > 100:
                self.fuel = 100
            print(f"{self.brand} {self.model} заправлено на {amount} л. Поточний рівень: {self.fuel} л.")
        else:
            print("некоректна кількість пального.")

    def show_info(self):

        status = "Запущений" if self.is_running else "Зупинений"
        print(f"\nАвтомобіль: {self.brand} {self.model}")
        print(f"Статус: {status}")
        print(f"Пробіг: {self.mileage} км")
        print(f"Пальне: {self.fuel} л\n")


car = Car("Mitsubishi", "ASX")

car.show_info()

car.start()

car.drive(200)

car.stop()

car.show_info()