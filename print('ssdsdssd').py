file = open('text2.txt', 'r')
# for line in file:
#     print(line)

mas=[]
for line in file:
    s=int(line.replace(  '\n', ''))
    s+= 10
    mas.append(s)

print(mas)
file.close()

st=str(mas)
a=open('f.txt', 'w')

a.write(st)
    
file=open('g.txt', 'r', encoding='utf-8')
s = input('Введите имя, которое нужно найти:')

for line in file:
    if line.replace('\n', '') == s:
        print('имя найдено')






