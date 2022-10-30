class Character:
    agility = 1
    strength = 1
    intellect = 1
    level = 1
    m_stat_name = ""
    m_stat = 1
    name = ""
    health = 100 * (strength / 10)
    damage = 1 * (m_stat / 10)
    defence = 1 * (agility / 10)
    dodge = 0
    mana = 50 * (intellect / 20)

    def __init__(self, name, health, damage, defence, intellect, strength, agility, level, dodge, mana, m_stat, m_stat_name):
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

    def __str__(self):
        return f"{self.name} \n" \
               f"Здоровье - {self.health}\n" \
               f"Сила - {self.strength}\n" \
               f"Ловкость - {self.agility}\n" \
               f"Интелект - {self.intellect}\n" \
               f"Урон - {self.damage}\n " \
               f"Мана - {self.mana}\n" \
               f"Основной Стат - {self.m_stat_name}\n" \
               f"Броня - {self.defence}\n" \
               f"Шанс уаорота - {self.dodge}\n"






























