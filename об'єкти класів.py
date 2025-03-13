import random

class Entrepreneur:
    def init(self, name):
        self.name = name
        self.money = 1000
        self.energy = 50
        self.motivation = 50
        self.alive = True
        self.days = 0

    def check_status(self):
        if self.money <= 0 or self.energy <= 0 or self.motivation <= 0:
            self.alive = False
            print(f"\n{self.name} збанкрутував! Гра закінчена.")
        elif self.money > 50000:
            self.alive = False
            print(f"\nВітаємо! {self.name} став успішним підприємцем!")

    def work(self):
        if self.alive:
            profit = random.randint(200, 500)
            self.money += profit
            self.energy -= random.randint(5, 15)
            self.motivation -= random.randint(5, 10)
            print(f"{self.name} працює. Прибуток: {profit}. Гроші: {self.money}, Енергія: {self.energy}, Мотивація: {self.motivation}")

    def invest(self):
        if self.alive and self.money >= 500:
            investment = random.randint(500, 2000)
            self.money -= investment
            if random.random() < 0.5:  # 50% шанс на успіх
                profit = investment * random.uniform(1.5, 3.0)
                self.money += int(profit)
                print(f"{self.name} успішно інвестував! Прибуток: {int(profit)}. Гроші: {self.money}")
            else:
                loss = investment * random.uniform(0.3, 0.7)
                self.money -= int(loss)
                print(f"{self.name} невдало інвестував! Втрата: {int(loss)}. Гроші: {self.money}")
        else:
            print("Недостатньо грошей для інвестицій.")

    def relax(self):
        if self.alive:
            self.energy += random.randint(10, 20)
            self.motivation += random.randint(10, 15)
            print(f"{self.name} відпочиває. Енергія: {self.energy}, Мотивація: {self.motivation}")

    def network(self):
        if self.alive:
            self.motivation += random.randint(5, 15)
            if random.random() < 0.3:  # 30% шанс знайти бізнес-можливість
                bonus = random.randint(500, 1500)
                self.money += bonus
                print(f"{self.name} знайшов бізнес-можливість! Прибуток: {bonus}. Гроші: {self.money}")
            print(f"{self.name} займався нетворкінгом. Мотивація: {self.motivation}")

    def simulate(self):
        while self.alive and self.days < 365:
            self.days += 1
            print(f"\nДень {self.days}:")
            action = random.choice([self.work, self.invest, self.relax, self.network])
            action()
            self.check_status()

# Запуск симуляції
name = input("Введіть ім'я підприємця: ")
entrepreneur = Entrepreneur(name)
entrepreneur.simulate()