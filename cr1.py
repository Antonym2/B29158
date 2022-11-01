import random
class Character:
    dodge_chance = 0
    agility = 1
    strength = 1
    intellect = 1
    level = 1
    to_next_level = 10
    m_stat_name = ""
    name = ""
    health = 100
    damage = 1
    defence = 1
    dodge = 0
    mana = 50
    choice = ""

    def __init__(self, name, health, damage, defence, intellect, strength, agility, level, dodge, mana, m_stat_name, to_next_level):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.intellect = intellect
        self.strength = strength
        self.agility = agility
        self.level = level
        self.dodge = dodge
        self.mana = mana
        self.m_stat_name = m_stat_name
        self.to_next_level = to_next_level

    def __str__(self):
        return f"{self.name} Уровень - {self.level}  До След. Уровня - {self.level}\n" \
               f"Здоровье - {self.health}\n" \
               f"Сила - {self.strength}\n" \
               f"Ловкость - {self.agility}\n" \
               f"Интелект - {self.intellect}\n" \
               f"Урон - {self.damage}\n" \
               f"Мана - {self.mana}\n" \
               f"Основной Стат - {self.m_stat_name}\n" \
               f"Броня - {self.defence}\n" \
               f"Шанс уворота - {self.dodge}\n"

    def stats_and_level(self):
        self.defence += self.agility / 4
        self.mana += self.intellect / 2
        self.health += self.strength / 4
        if self.m_stat_name == "agility":
            self.damage += self.agility / 2
        if self.m_stat_name == "strength":
            self.damage += self.strength / 2
        if self.m_stat_name == "intellect":
            self.damage += self.intellect / 2

    def take_damage(self, damage):
            self.health -= damage


    def attack(self, player):
        if player.fight == True:
            dodge_chance = random.randint(1, 100)
            if self.health > 0:
                print(f"Жив(ая) - {self.name}")
                if dodge_chance < player.dodge:
                    player.take_damage(0)
                    print(f"Уворот так как dodge_chance {dodge_chance} < player.dodge {player.dodge}")
                else:
                    if player.defence > self.damage:
                        player.take_damage(0)
                    else:
                        player.take_damage(self.damage - player.defence)
            else:
                print(f"Погиб - {player.name}")
                print("Бить труп плохо")
                player.fight = False

    def defece(self):
        pass


    def fight(self, player, choice):
        player.stats_and_level()
        self.stats_and_level()
        while True:
            print(f"Уровень - {self.level}-------1-й игрок (вы) {self.name}------------2-й игрок-{player.name}-Уровень - {player.level}\n"
                  f"1-й игрок (вы)---------------------------------------------2-й игрок\n"
                  f"Здоровье - {self.health}                                     Здоровье - {player.health}\n" 
                   f"Сила - {self.strength}                                          Сила - {player.strength}\n" 
                   f"Ловкость - {self.agility}                                      Ловкость - {player.agility}\n" 
                   f"Интелект - {self.intellect}                                       Интелект - {player.intellect}\n" 
                   f"Урон - {self.damage}                                         Урон - {player.damage}\n" 
                   f"Мана - {self.mana}                                         Мана - {player.mana}\n" 
                   f"Основной Стат - {self.m_stat_name}                            Основной Стат - {player.m_stat_name}\n" 
                   f"Броня - {self.defence}                                          Броня - {player.defence}\n" 
                   f"Шанс уворота - {self.dodge}                                  Шанс уворота - {player.dodge}\n")
            self.choice = input("ваше действие:\n 1-атака, \n2-защита, \n3-сдатся \n")
            if self.choice == "1":
                self.attack()
            elif self.choice == "2":
                self.defece()
            elif self.choice == "3":
                self.health == 0













