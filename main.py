from random import randint
from time import sleep
from operator import itemgetter
game = {'Player1': randint(1, 6),
        'Player2': randint(1, 6),
        'Player3': randint(1, 6),
        'Player4': randint(1, 6)}
ranking = list()
print('Raffled values:')
for k, v in game.items():
    print(f'{k} equals \033[1;32m{v}\033[m in dice')
    sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('====== RANKING OF PLAYER ======')
for i, v in enumerate(ranking):
    print(f'   \033[1;33m{i+1}\033[m place: {v[0]} with \033[1;32m{v[1]}\033[m.')
    sleep(1)
