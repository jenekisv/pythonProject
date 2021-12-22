print('rabota s peremennimi')
x = 12
y = 2
print(x * 3)
print(x - y)
print('virajeniy v strokah, umnojenie')
print('hi ' * 4)
print(4 * '2')
print('virajeniy v strokah, slojenie')
print('2' + '2')
print('h' + 'i')
print('propusk stroki')
print()
print("hi")
print('hi')
print(5 + 6)
print((2 + 2) * 5)
print((2 / 2) * 5)
print('net deleniy, primer')
# print(5/0)
print(3 / 4)
print(8 / 2)
print('operacii s drobnimi')
print(6 * 7.0)
print(4 + 1.65)
print('vozvedenie v stepen')
print(2 ** 5)
print(9 ** (1 / 2))
print((1 + 3) ** 2)
print('celochislennoe delenie, bez ostatka')
print(20 // 6)
print('ostatok ot deleniy')
print(20 % 6)
print('avtomaticheskiy perenos stroki, troinie kavichki')
print("""11111 11111 11111 11111 11111""")
print('ekran kavichek, perenos stroki, otstup')
print('\"hi\" \n\thi')
# name = input()
# age = input()
# print(name + ' imeet ' + age)
x = 5
x *= 3
print(x)
x = 'Hi '
x += 'Evgeniy'
print(x)
print('operator ravenstva')
print(3 == 2)
print('operator neravenstva')
print(3 != 7)
print('operator sravnenia')
print(5 > 5)
print('operator sravnenia ravenctvaa')
print('ane' >= 'anc')
print('\n instukcii if, else')
x = 5
if x >= 7:
    print('ok')
else:
    print('no')
num = 4
if num == 1:
    print('1')
else:
    if num == 2:
        print('2')
    else:
        if num == 3:
            print('3')
        else:
            print('net vernova otveta')
print('\n instrukcia elif')
num = 3
if num == 1:
    print('1')
elif num == 2:
    print('2')
elif num == 3:
    print('3')
else:
    print('net vernova otveta')
print('\n operatori and, or, not')
print('buleva logika -and- oba znachenia istina')
print(1 == 1 and 2 + 2 > 3)
print('buleva logika -and- tolko odno istina libo oba loj')
print(2 == 2 and 2 == 3)
print(1 == 2 and 2 < 1)
print('buleva logika -or- oba znachenia istina libo odno')
print(1 == 1 or 2 > 1)
print(1 == 1 or 1 > 5)
print('beleva logika -or- oba znachenia loj')
print(1 != 1 or 1 > 5)
print('buleva logika -not- ne loj, ne pravda')
print(not 1 > 7)
print(not 9 == 9)
print('\n prioritet operatorov')
print(
    """\n\t kak v matematike - snachalo skobki, potom vozvedenie v stenen, dalee umnojenie i delenie, poslednie slojenie i vichitanie""")
grayd = 80
if (grayd >= 70 and grayd <= 90):
    print('\n verno')
print(
    """\n rabota so spiskami -list- v kvadratnih skobkah, indeks spiska vsegda nachinaetsa s 0 i ukazivaetsa v kvadratnih skobkah""")
print()
worlds = ['Hello', 'World', '!']
print(worlds[0])
print(worlds[1])
print(worlds[2])
print('\n sozdanie pustova spiska')
ochered = []
print(ochered)
print('\n sozdanie spiska, vnutri spiska')
number = 3
mylit = ["string", 0, 2, 3,
         [4, 5, number],
         1]
print(mylit[0])
print(mylit[2])
print('vivod 3 simvola stroki -string- mylit')
print(mylit[0][2])
print('\n vivod 3 simvola, 2 tablici mis')
mis = [
    [1, 2, 3],
    [4, 5, 6]
]
print(mis[1][2])
print('\n rabota s indeksom stroki')
str = "Privet!"
print(str)
print(str[3])
print('\n perenaznachenie elementa spiska')
nums = [7, 7, 7, 7, 7]
print(nums)
nums[2] = 5
print(nums)
print('\n operacii so spiskami, slojenie, umnojenie')
num1 = [1, 2, 3]
print(num1 + [4, 5, 6])
print(num1 * 3)
print('\n proverit nalichie v spiske')
wor = ["odin", "dva", "tri", "chetiri"]
print("odin" in wor)
print("dva" in wor)
print("tomp" in wor)
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
print("""\n funkcii spiska, metod -append- dobavlenie elimenta v konec spiska""")
nums = [1, 2, 3]
nums.append(4)
print(nums)
print('\n funkcia -len- podschet elementov v spiske')
nums = [1, 2, 3, 4, 5, 6]
print(len(nums))
print('''\n metod -insert- pozvolaet vstavit element v spisok na lubuu poziciu''')
worlds = ["odin", 'odin']
# print('1 sposob')
index = 1
worlds.insert(index, 'is')
# print('2 sposob, uproschenii')
worlds.insert(1, 'tochno')
print(worlds)
print('\n metodi:')
spiska = ['a', 'b', 'c', 'd', 'e', 'f']
print('\n -index- naidet pervoe upominanie elementa v splske i vivedit ego index')
print(spiska.index('c'))
print('\n -max(list)- vozvrat elementa s maksimalnim znacheniem i minimalnim znacheniem -min(list)-')
print(max(spiska))
print(min(spiska))
print('\n -list.count(obj)- kol-vo upominaniy v spiske')
print(spiska.count('d'))
print('\n -list.remove(obj)- udalenie obekta iz spiska')
spis = ['a', 'b', 'c', 'd', 'e', 'f']
print(spis.remove('a'))
print(spis)
print('\n -list.reverse()- raspolojit elementi v obratnom poradke')
sp = ['a', 'b', 'c', 'd', 'e', 'f']
print(sp.reverse())
print(sp)
print('\n cikl -while- ciklicheskoe povtorenie')
i = 1
while i <= 5:
    print(i)
    i = i + 1
    print('Vipolneno!')
print('\n vipolnenia cikla 4 raza ot 3 do 0')
i = 3
while i >= 0:
    print(i)
    i = i - 1
    print('ok')
    print('\n operatori if/else vnutri cicla while')
chis = 0
while chis < 10:
    if chis % 2 == 0:
        print(chis)
    else:
        print()
    chis += 1
print('\n sozdanie beskonechnih ciklov -while True:- ostanovka operatorom -break-')
i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break
print('\n operator -continue-')
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        print('propuscheno 3')
        continue
