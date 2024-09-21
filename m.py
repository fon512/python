
import time


hp = 100
mana = 100
сила = 6
ловкасть = 12
intellect = 6
lvl = 1
print("здоровье:",mana, hp, сила)
print(f'сила:{сила}  \nловкость:{ловкасть}')
print(mana * hp)
input('харектеристика:')
print(f'здоровье:{hp},мана:{mana},сила:{сила},ловкасть:{ловкасть},интелект:{intellect}')
name = input('введите имя персонажа:')
print(f'добро пажаловать, {name}')

_class = input('выберите класс: 1. воин, 2. маг, 3. вор\n')

if _class == 'воин' or _class == "1":
    сила *=  2
    ловкасть *= 2
    _class = 'воин'
elif _class == 'маг' or _class == "2":
    mana += 80
    intellect +=  5
    _class = 'маг'
elif _class == "вор" or _class == "3":
    сила *= 2
    mana += 35
    ловкасть *= 1.5
    _class="вор"
else:
    print('ОШИБКА КЛАСС НЕ НАЙДЕН, дан класс НИЩИЙ. \n Все характеристики понижены на 3')
    сила /= 1.2
    ловкасть /= 2
    intellect /= 1.5
    mana -= 75
    hp -= 50
    _class = 'НИЩИЙ'
print(f"Ваш новый класс: {_class}, новые характеристики:\nСила: {сила}\nЛовкость: {ловкасть}\nИнтелект: {intellect}\nmana: {mana}\nоз: {hp}")

# for i in range(100):
#     print('проход по циклу (итерация) №', i)

# n = 11
#
# while n<10:
#      print('цикл работает', n)
#      n = n + 1
#      #break
# else:
#     print('выполнился else')

isgame = True
while isgame == True:
    print('Игра идёт')
    hp -= 1
    print('остаток здоровья:', hp)
    if hp <= 0:
        print('ПОТРАЧИНО')
        isgame = False
        break
    time.sleep(0.5)
print('игра завершена')
