import time
import random
# название = значение

hp = 100
mana = 100
strength = 5
agility = 5
intellect = 5
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
    _class = "Воин" 

elif _class == "маг" or _class=="2":
    intellect *= 2
    agility *= 1.3
    _class="Маг"
elif _class == "вор" or _class=="3":
    agility *= 2
    strength *= 1.5
    intellect *= 1.3
    _class="Вор"
else: 
    print("ФАТАЛЬНАЯ ОШИБКА, ты НИЩИЙ.\nВсе характеристики понижены на 3")
    strength -= 3
    agility -= 3
    intellect -= 3
    _class = "НИЩИЙ"

print(f"Ваш новый класс: {_class}, новые характеристики:\nСила: {strength}\nЛовкость: {agility}\nИнтеллект: {intellect}")

# ctrl + /

# for i in range(100):
#     print("Проход по циклу (итерация) №", i)

# n = 11

# while n<10:
#     print("Цикл работает", n)
#     n = n + 1
# else: 
#     print("выполнился else")



isGame = True
# while isGame == True:
while isGame:
    # hp -= 1
    rand = random.randint(1,6)

    print("выпало", rand)

    if rand == 2:
        print("На пути Тролль, -15хп")
        hp -= 15
        time.sleep(1.5)
    print("Остаток здоровья:", hp)
    if hp <= 0:
        print("ПОТРАЧЕНО")
        isGame = False
        break
    time.sleep(0.5)
    
print("Игра завершена")