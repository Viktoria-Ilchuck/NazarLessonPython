import random

class Entrepreneur:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.energy = 100
        self.motivation = 100
        self.alive = True

    def work(self):
        profit = random.randint(500, 1500)
        self.money += profit
        self.energy -= 10
        self.motivation -= 5
        print(f"{self.name} попрацювала і заробила {profit} грн.")

    def invest(self):
        if self.money < 500:
            print("Недостатньо грошей для інвестування.")
            return

        self.money -= 500
        chance = random.random()
        if chance < 0.4:
            loss = random.randint(200, 500)
            self.money -= loss
            print(f"Інвестиція не вдалася. Втрата {loss} грн.")
        else:
            gain = random.randint(1000, 5000)
            self.money += gain
            print(f"Успішна інвестиція! Прибуток {gain} грн.")

        self.motivation -= 5
        self.energy -= 5

    def relax(self):
        self.energy += 15
        self.motivation += 10
        print(f"{self.name} відпочила.")

    def network(self):
        self.motivation += 5
        if random.random() < 0.3:
            bonus = random.randint(500, 2000)
            self.money += bonus
            print(f"{self.name} знайшла можливість і заробила {bonus} грн.")
        else:
            print(f"{self.name} завела нові контакти.")

        self.energy -= 5

    def check_status(self):
        if self.money <= 0 or self.energy <= 0 or self.motivation <= 0:
            self.alive = False
            print(f"{self.name} зазнала поразки в бізнесі...")
        elif self.money >= 50000:
            self.alive = False
            print(f"{self.name} досягла успіху в бізнесі!")


def run_simulation(name):
    player = Entrepreneur(name)

    for day in range(1, 366):
        if not player.alive:
            break
        print(f"\nДень {day}")
        action = random.choice(["work", "invest", "relax", "network"])
        if action == "work":
            player.work()
        elif action == "invest":
            player.invest()
        elif action == "relax":
            player.relax()
        elif action == "network":
            player.network()

        player.check_status()
        print(f"Баланс: {player.money}, Енергія: {player.energy}, Мотивація: {player.motivation}")

    if player.alive:
        print("\n365 днів завершено.")
        if player.money >= 50000:
            print(f"Вітаємо, {name} стала успішним підприємцем!")
        else:
            print(f"{name} не досягла цілі, але вижила у бізнесі.")


run_simulation("Вікторія")