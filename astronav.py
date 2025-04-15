import random


class Alien:
    def __init__(self, species, attitude, technology_level, trade_items):
        self.species = species
        self.attitude = attitude
        self.technology_level = technology_level
        self.trade_items = trade_items

    def trade(self, astronaut):
        if self.attitude == 'дружній' and self.trade_items:
            item = random.choice(self.trade_items)
            astronaut.inventory.append(item)
            print(f"Інопланетянин поділився: {item}")
        else:
            print("Інопланетянин не хоче торгувати.")

    def attack(self, astronaut):
        damage = random.randint(10, 30)
        astronaut.energy -= damage
        print(f"Інопланетянин атакував! Втрачено {damage} енергії.")

    def negotiate(self, astronaut):
        success = random.random() < 0.5
        if success:
            self.attitude = 'дружній'
            print("Успішні переговори!")
        else:
            print("Переговори провалено.")
            self.attack(astronaut)


class Planet:
    def __init__(self, name, resources, habitable, gravity, aliens):
        self.name = name
        self.resources = resources
        self.habitable = habitable
        self.gravity = gravity
        self.aliens = aliens

    def discover_resources(self):
        print(f"Планета {self.name} має ресурси: {', '.join(self.resources)}")


class Spaceship:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.hull_strength = 100
        self.upgrades = []

    def travel(self, planet):
        if self.fuel >= 20:
            self.fuel -= 20
            print(f"Подорож до {planet.name} виконано. Паливо: {self.fuel}")
            return True
        else:
            print("Недостатньо пального.")
            return False

    def add_upgrade(self, upgrade):
        self.upgrades.append(upgrade)
        print(f"Корабель покращено: {upgrade}")


class Astronaut:
    def __init__(self, name, spaceship):
        self.name = name
        self.oxygen = 100
        self.energy = 100
        self.inventory = []
        self.spaceship = spaceship

    def mine_resources(self, planet, desired_resource="уран"):
        if desired_resource in planet.resources:
            self.inventory.append(desired_resource)
            print(f"{self.name} зібрала уран!")
        elif planet.resources:
            res = random.choice(planet.resources)
            self.inventory.append(res)
            print(f"{self.name} зібрала ресурси: {res}")
        else:
            print("Ресурси не виявлено.")
        self.energy -= 10
        self.oxygen -= 5

    def upgrade_ship(self, resource):
        if resource in self.inventory:
            self.inventory.remove(resource)
            self.spaceship.add_upgrade(f"Покращення з {resource}")
        else:
            print(f"{resource} не знайдено в інвентарі.")

    def communicate_with_aliens(self, alien):
        print(f"Контакт з расою {alien.species} ({alien.attitude})")
        if alien.attitude == 'дружній':
            alien.trade(self)
        else:
            alien.negotiate(self)

    def explore(self, planet):
        print(f"{self.name} досліджує {planet.name}")
        planet.discover_resources()
        if planet.aliens:
            for alien in planet.aliens:
                self.communicate_with_aliens(alien)
        else:
            print("Інопланетян не виявлено.")

    def survive_in_space(self):
        warnings = []
        if self.oxygen <= 20:
            self.oxygen += 30
            warnings.append("Критичний рівень кисню!")
        if self.energy <= 20:
            self.energy += 30
            warnings.append("Критичний рівень енергії!")
        self.oxygen -= 5
        self.energy -= 5
        for warning in warnings:
            print(warning)
        if self.oxygen <= 0 or self.energy <= 0:
            print(f"{self.name} загинула у космосі.")
            return False
        return True

def generate_planets():
    names = ["Марс", "Венера", "Нептун", "Сатурн", "Плутон", "Глізе", "Альфа", "Зета"]
    resources_pool = [["уран", "залізо"], ["кристали"], ["вода", "уран"], ["газ", "метал"],
                      ["лід"], ["уран", "платина"], ["мінерали", "кремній"], ["кремній", "уран"]]
    planets = []
    for i in range(len(names)):
        aliens = []
        if random.random() < 0.6:
            aliens.append(Alien("Добрі Кукозікі", "дружній", 8, ["технологія", "мінерали"]))
        if random.random() < 0.4:
            aliens.append(Alien("Злі Бубозікі", "ворожий", 6, []))
        planet = Planet(
            names[i],
            resources_pool[i],
            habitable=random.choice([True, False]),
            gravity=round(random.uniform(0.5, 2.0), 2),
            aliens=aliens
        )
        planets.append(planet)
    return planets


def play_game():
    ship = Spaceship("StarSeeker")
    hero = Astronaut("Катерина", ship)
    planets = generate_planets()

    for _ in range(2):
        planet = random.choice(planets)
        print("\n--- Нова подорож ---")
        if ship.travel(planet):
            hero.explore(planet)
            hero.mine_resources(planet, desired_resource="уран")
            if hero.inventory:
                res = random.choice(hero.inventory)
                hero.upgrade_ship(res)
            if not hero.survive_in_space():
                break

    print("\n--- КІНЕЦЬ ГРИ ---")
    print(f"Інвентар: {hero.inventory}")
    print(f"Покращення корабля: {ship.upgrades}")


if __name__ == "__main__":
    play_game()