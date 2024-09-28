# i = 1
# while i <= 100:
#     print(i, '0')
#     i += 1

# s=1
# for t in range (1,101):
#     s += t
#     print('t',t)
#     print('s',s)
# print(s)
# an=int(input('введити число:'))
#
#
# s=0
# for t in range (1, an):
#  if t%2!= 0:
#
#      s += t
#      print('t',t)
#      print('s',s)
# print(s)

while  True:

    print('добро пажаловать на ответь на вопросы и выйграй 1000р')
    www = input('как вас завут:')
    print("хорошо",www)
    print('1 вопрос')
    print('сколько 2+2?')
    print('А.22')
    print('Б. 2')
    print('В. 4')
    print('Г. 5')
    bank= 0
    ans1=input('Ответ - ')

    if ans1 == 'В' or ans1 == 'В':
        print('Это правильный ответ')
        bank +=250
        print('Твой банк:', str(bank))
    else:
        print('славу богу ответ неправильный')
        print('Игра окончена')
        print('Твой банк',str(bank))
        break











