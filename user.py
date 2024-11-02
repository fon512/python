user = {
    'username': 'кто ты воин',
    'password': 1234,
    'robux': 100500,
    'age': 74,
    'genger': 'мужчина'
} 



print('имя пользователя', user['username'])
print('у вас', user['robux'], 'роблоксов')

#user.clear()
#print('после clear', user)

print(user.get('genger'))# тоже самое как и user['genger']
print(user.items())
print(user.keys())
print(user.pop('robux'))
print(user)
print(user.values())

print(user)
#добавление в словарь новое свойство
user['robux'] = 12345678
print(user)



user.setdefault('new key', 'мое новое значение')

print(user)



player = {
    'name':'bobo',
    'hp':120,
    'damage':15
}

enemy = {
    'name':'baba',
    'hp': 100,
    'damage': 10
}

def Fight(player=user, enemy=enemy):
    print(f"Игрок {player['name']} атакует {enemy['name']} и наносит {player['damage']}")
    enemy['hp'] -= player['damaga']
    print(f"у {enemy['name']} осталось {enemy['hp']} здоровье")

Fight(player, enemy)
