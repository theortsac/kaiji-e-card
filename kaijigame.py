from random import randrange

kingCards = ['C', 'C', 'C', 'C', 'K']
slaveCards = ['C', 'C', 'C', 'C', 'S']
print("""- C = Citizen
- S = Slave
- K = King""")
for i in range(5):
    print('Your cards:', slaveCards)
    cardIPlay = input('Which card will you play? ')
    slaveCards.remove(cardIPlay)
    cardKPlay = kingCards[randrange(len(kingCards))]
    kingCards.remove(cardKPlay)
    print('The enemy played', cardKPlay + '!')
    if cardIPlay == 'S' and cardKPlay == 'C':
        print('Defeated!')
        break
    elif cardIPlay == 'C' and cardKPlay == 'K':
        print('Defeated!')
        break
    elif cardIPlay == 'S' and cardKPlay == 'K':
        print('Victory!')
        break
    else:
        print('Draw!')
