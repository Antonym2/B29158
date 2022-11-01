from cr1 import Character
player1 = Character(name="Phantom Asasin", agility=40, strength=12, intellect=8, health=500, damage=105, defence=8, level=1, dodge=20, mana=120, m_stat_name="agility", to_next_level=10)

player2 = Character(name="Axe", agility=11, strength=38, intellect=8, health=860, damage=79, defence=9, level=1, dodge=0, mana=80, m_stat_name="strength", to_next_level=10)

player3 = Character(name="Lion", agility=9, strength=9, intellect=32, health=480, damage=66, defence=2, level=1, dodge=0, mana=280, m_stat_name="intellect", to_next_level=10)

player4 = Character(name="Lich", agility=5, strength=11, intellect=29, health=540, damage=54, defence=3, level=1, dodge=0, mana=300, m_stat_name="intellect", to_next_level=10)

player1.fight(player2)
