from AVLTree import *
from Music import *

m1 = Music('misunderstood', 'bon jovi', 'bounce', 2002)
m2 = Music('buried alive', 'avenged sevenfold', 'nightmare', 2010)
m3 = Music('nightrain', 'guns n roses', 'appetite for destruction', 1987)
m4 = Music('highway to hell', 'acdc', 'highway to hell', 1979)
m5 = Music('wasting love', 'iron maiden', 'fear of the dark', 1992)
m6 = Music('never too late', 'three days grace', 'one-x', 2006)
m7 = Music('fade to black', 'metallica', 'ride the lightning', 1984)
m8 = Music('carry on', 'angra', 'angles cry', 1993)
m9 = Music('i want out', 'helloween', 'keep of the seven keys part 2', 1988)
m10 = Music('paradise', 'stratovarius', 'fouth dimension', 1995)
m11 = Music('boom', 'system of a down', 'steal this album', 2002)
m12 = Music('you and i', 'scorpions', 'pure instinct', 1996)

playlist = AVLTree()
root = None
root = playlist.insert(root, m1.name, m1)
root = playlist.insert(root, m2.name, m2)
root = playlist.insert(root, m3.name, m3)
root = playlist.insert(root, m4.name, m4)
root = playlist.insert(root, m5.name, m5)
root = playlist.insert(root, m6.name, m6)
root = playlist.insert(root, m7.name, m7)
root = playlist.insert(root, m8.name, m8)
root = playlist.insert(root, m9.name, m9)
root = playlist.insert(root, m10.name, m10)
root = playlist.insert(root, m11.name, m11)
root = playlist.insert(root, m12.name, m12)

while True:
    arqmenu = open('menu.txt', 'r')
    print(f"{'-= MENU =-':=^40}")
    for linha in arqmenu:
        print(linha, end='')
    print('-==-' * 10)
    arqmenu.close()

    op = int(input("Option:\n>>> "))

    if op == 1:

        name = str(input("Music name: ")).lower()
        author = str(input("Author: ")).lower()
        album = str(input("Album: ")).lower()
        year = int(input("Year: "))

        song = Music(name, author, album, year)
        search = playlist.search(root, song.name)
        if not search:
            root = playlist.insert(root, song.name, song)
            if root:
                print('Success')

        else:
            print('Its not possible duplicate records')

    if op == 2:

        name = str(input("Music name: ")).lower()
        search = playlist.search(root, name)
        if search:
            print(search)
        else:
            print("There's no record with that key")

    if op == 3:

        year = int(input("Input year: "))

        result = playlist.searchByYear(root, year)
        print(f'{"MUSIC BY YEAR":=^40}')
        print(f'{year}:')
        print()
        for song in result:
            print(song)
        print()
        print('-==-' * 10)

    if op == 4:

        rem = str(input("Music name: ")).lower()
        search = playlist.search(root, rem)
        if search:
            playlist.remove(root, rem)
            if root:
                print('Success')

        else:
            print("There's no record with that key")

    if op == 5:

        playlist.inOrder(root)

    if op == 6:

        print(f'Deepness: {playlist.deep(root)}')
        print(f'Number of Keys: {playlist.numberOfNodes(root)}')

    if op == 7:

        print('GoodBye!')
        break
