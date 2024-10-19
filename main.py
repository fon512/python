import time
import random

enemy = {
    'name':'Орк',
    'damage':15,
    'hp':45,
    'armor':4
}
enemy['hp'] = 30
print(enemy['hp'])

massEnemies = ['Гоблин', 'Орк', 'слизь', 'скилет',{'name':'Орк',
    'damage':15,
    'hp':45,
    'armor':4}]

# print(massEnemies[0])
# print(len(massEnemies)-1)
# print(massEnemies[len(massEnemies)-1])
#
# massEnemies.append(123)
# print(massEnemies)
# massEnemies.remove(123)
# print(massEnemies)
# massEnemies.pop(0)
# print(massEnemies)
# название = значение

hp = 100
mana = 100

strength = 5
agility = 5
intellect = 5

damage = 5
protection = 5

lvl = 1

print("Здоровье:", hp, "Мана:", mana)
print(f"Сила: {strength}\nЛовкость: {agility}\nИнтеллект: {intellect}")
name = input("Введите имя персонажа: ")
print(f"Приветствуем вас, {name}!")

_class = input("Выберите класс: 1. воин, 2. маг, 3. вор\n")
# Если класс ВОИН - умножаем силу на 2, а ловкость на 1.6
# Если класс МАГ - умножаем интеллект на 2, а ловкость на 1.3
# Если класс ВОР - умножаем ловкость на 2, а силу на 1.5, а интеллект на 1.3
# > < == >= <= !=
if _class == "воин" or _class == "1":
    strength = strength * 2
    agility *= 1.6
    protection += 5
    damage += 2
    hp += 50
    _class = "Воин"
elif _class == "маг" or _class == "2":
    intellect *= 2
    agility *= 1.3
    protection -= 3
    damage += 3
    mana += 50
    _class = "Маг"
elif _class == "вор" or _class == "3":
    agility *= 2
    strength *= 1.5
    intellect *= 1.3
    damage -= 1
    protection -= 2
    _class = "Вор"
else:
    print("ФАТАЛЬНАЯ ОШИБКА, ты НИЩИЙ.\nВсе характеристики понижены на 3")
    strength -= 3
    agility -= 3
    intellect -= 3
    _class = "НИЩИЙ"

print(
    f"Ваш новый класс: {_class}, новые характеристики:\nСила: {strength}\nЛовкость: {agility}\nИнтеллект: {intellect}")

# for i in range(100):
#     print("проход по циклу (итерация) №", i)

# n = 0

# while n<10:
#     print("цикл работает")
#     n = n + 1
# else:
#     print("выполнился else")

isGame = True
while isGame:
    # print("Игра идёт")
    # hp -= 1
    rand = random.randint(0, len(massEnemies)+10)
    # rand = random.choice(massEnemies)


    if len(massEnemies)>rand and massEnemies[rand] == 'Гоблин' :
        enemyName = massEnemies[rand]
        hpEnemy = 20
        damageEnemy = 7
        print(f'\nперед вами {enemyName} что делать?')
        while True:

            choice = input('\n1. Атоковать 2. Защититься 3. увернутся\n')

            if choice == '1':
                hpEnemy -= damage
                hp -= damageEnemy // 1.5
                print(f'{enemyName.capitalize()} получил урон у него осталось {hpEnemy} hp')
                print(f'хоть ты и ударил но и тебе тоже прилетело{damageEnemy // 1.5} урона\n у вас осталось {hp} hp')
                print(f'{enemyName.capitalize()} получил урон у него осталось {hpEnemy}')
            elif choice == "2":
                if damageEnemy > damage:
                    hp = hp - (damageEnemy - damage)
                    print(f"{enemyName.capitalize()} наносит {damageEnemy - damage} урон у вас осталось hp-{hp}")
                else:
                    print('Вы успешно заблокировали урон')
            elif choice == '3':

                rand = random.randint(1, 2)
                if rand == 1:
                    print('Успешный уворот')
                else:
                    hp -= damageEnemy
                    print(f'Увернутся не получилось, вы полочили урон {damageEnemy}')
            else:
                hp -= damageEnemy
                print(f'вы так и не выбрали правельного решения и вас ударили вы потеряли {damageEnemy}hp')
            if hp <= 0:
                break
            elif hpEnemy <= 0:
                print('вы победили')
                break
    time.sleep(0.5)

    print("Остаток здоровья:", hp)
    if hp <= 0:
        print("GAME OVER")
        isGame = False
        break

    time.sleep(0.5)
    if rand == 4:
        enemyName = massEnemies[rand]['name'] == 'Орк'
        hpEnemy = massEnemies[rand]['hp']
        damageEnemy = massEnemies[rand]['armor']
        print('перед вами Орк что делать?')
        while True:
            choice = input('\n1. Атоковать 2. Защититься 3. увернутся\n')

            if choice == '1':
                hpEnemy -= damage
                hp -= damageEnemy // 1.5
                print(f'Орк получил урон у него осталось {hpEnemy} hp')
                print(f'хоть ты и ударил но и тебе тоже прилетело{damageEnemy // 1.5} урона\n у вас осталось {hp} hp')
                print(f'Орк получил урон у него осталось {hpEnemy}')
            elif choice == "2":
                if damageEnemy > damage:
                    hp = hp - (damageEnemy - damage)
                    print(f"Орк наносит {damageEnemy - damage} урон у вас осталось hp-{hp}")
                else:
                    print('Вы успешно заблокировали урон')
            elif choice == '3':

                rand = random.randint(1, 2)
                if rand == 1:
                    print('Успешный уворот')
                else:
                    hp -= damageEnemy
                    print(f'Увернутся не получилось, вы получили урон {damageEnemy}')
            else:
                hp -= damageEnemy
                print(f'вы так и не выбрали правильное решения и вас ударили вы потеряли {damageEnemy}hp')
            if hp <= 0:
                break
            elif hpEnemy <= 0:
                print('вы победили')
                break
    time.sleep(1.5)

    print("Остаток здоровья:", hp)
    if hp <= 0:
        print("GAME OVER")
        isGame = False
        break
    time.sleep(0.5)





