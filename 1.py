count = 0

print('1. Какой металл был открыт Гансом Кристианом Эрстедом в 1825 г. \n а)Галлий \n б)Титан \n с)Золото \n г)Алюминий')
answer = input('Ответ:\n ')
if str(answer) == 'г' or str(answer) == 'Г':
    print('правильно\n')
    count += 1
    print(str(count) + ' + 1 очко\n')
elif len(answer) == 0:
    print('вы ничего не написали\n')
    print(str(count) + ' + ничего\n')
else:
    print('неверно\n')
    count -= 1
    print(str(count) + ' - 1 очко\n')

print('2. Какова продолжительность жизни стрекозы \n а)день \n б)12 часов \n с)год \n г)80 лет')
answer2 = input('Ответ:\n ')
if str(answer2) == 'а' or str(answer2) == 'А':
    print('правильно\n')
    count += 1
    print(str(count) + ' + 1 очко\n')
elif len(answer2) == 0:
    print('вы ничего не написали\n')
    print(str(count) + ' + ничего\n')
else:
    print('неверно\n')
    count -= 1
    print(str(count) + ' - 1 очко\n')

print('3. Какая самая маленькая птица в мире \n а)голубь \n б)колибри \n с)воробей \n г)сокол')
answer3 = input('Ответ:\n ')
if str(answer3) == 'б' or str(answer3) == 'Б':
    print('правильно\n')
    count += 1
    print(str(count) + ' + 1 очко\n')
elif len(answer3) == 0:
    print('вы ничего не написали\n')
    print(str(count) + ' + ничего\n')
else:
    print('неверно\n')
    count -= 1
    print(str(count) + ' - 1 очко\n')

print('4. Какой химический символ серебра \n а)Au \n б)Al \n с)Ag \n г)As')
answer4 = input('Ответ:\n ')
if str(answer4) == 'с' or str(answer4) == 'С':
    print('правильно\n')
    count += 1
    print(str(count) + ' + 1 очко\n')
elif len(answer4) == 0:
    print('вы ничего не написали\n')
    print(str(count) + ' + ничего\n')
else:
    print('неверно\n')
    count -= 1
    print(str(count) + ' - 1 очко\n')

print('5. Как называется крупнейшая технологическая компания в Южной Корее \n а)Samsung \n б)Xiaomi \n с)Huawei \n г)BQ')
answer5 = input('Ответ:\n ')
if str(answer5) == 'а' or str(answer5) == 'A':
    print('правильно\n')
    count += 1
    print(str(count) + ' + 1 очко\n')
elif len(answer5) == 0:
    print('вы ничего не написали\n')
    print(str(count) + ' + ничего\n')
else:
    print('неверно\n')
    count -= 1
    print(str(count) + ' - 1 очко\n')
print(f'конец викторины\n - вот очки \n - {count}')