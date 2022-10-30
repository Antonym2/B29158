import random
class Character:
    dodge_chance = 0
    agility = 1
    strength = 1
    intellect = 1
    level = 1
    to_next_level = 10 * (level / 2)
    m_stat_name = ""
    m_stat = 1
    name = ""
    health = 100 * (strength / 10) * (level/5)
    damage = 1 * (m_stat / 10) * (level/5)
    defence = 1 * (agility / 10)
    dodge = 0
    mana = 50 * (intellect / 20)

    def __init__(self, name, health, damage, defence, intellect, strength, agility, level, dodge, mana, m_stat, m_stat_name, to_next_level):
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
        self.m_stat = m_stat
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

    def take_damage(self, damage):
            self.health -= damage

    def attack(self, player):
        dodge_chance = random.randint(0, 100)
        if dodge_chance > self.dodge:
            player.take_damage(0)
        else:
            player.take_damage(self.damage)







