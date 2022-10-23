import random
fp_score = 0
fc_score = 0
choices = ["камень", "бумага", "ножницы"]
print("Камень > ножницы. Ножницы > бумагу. Бумага > камень.")
while True:
    p_score = 0
    c_score = 0
    player = input("Выберите: \nкамень (к), \nбумага(б), или \nножницы(н) \n(выйти) ? \n")
    player = player.lower()
    computer = random.choice(choices)
    print(f"Твой выбор: {player}, \nкомпьютер выбрал: {computer}.")
    if player == computer:
        print("Ничья")
    elif player == "камень" or player == "к":
        if computer == "ножницы":
            print("ты победил!")
            p_score += 1
            fp_score += 1
        else:
            print("Победил компьютер!")
            c_score += 1
            fc_score += 1
        print(f"Общий счёт: у вас {p_score} у компьютера {c_score}")
    elif player == "бумага" or player == "б":
        if computer == "камень":
            print("Ты победил!")
            p_score += 1
            fp_score += 1
        else:
            print("Победил компьютер!")
            c_score += 1
            fc_score += 1
        print(f"Общий счёт: у вас {p_score} у компьютера {c_score}")
    elif player == "ножницы" or player == "н":
        if computer == "бумага":
            print("Ты победил!")
            p_score += 1
            fp_score += 1
        else:
            print("Победил компьютер!")
            c_score += 1
            fc_score += 1
        print(f"Общий счёт: у вас {p_score} у компьютера {c_score}")
    elif player == "выйти":
        print(f"Общий финальный счёт: у вас {fp_score}\n у компьютера {fc_score}")
        break
    else:
        print("произошла ошибка...")
        player = input("Выберите: \nкамень (к), \nбумага(б), или \nножницы(н) \n(выйти) ? \n")