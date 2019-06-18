##Juego de pelea##
from random import randrange

vida_juagdor1 = 100
vida_juagdor2 = 100
##randrange(1,7)
turno = randrange(1,3)
golpe = (10,20)
banner ='''
   ██▀███   ▄▄▄       █    ██  ███▄    █   ▄████  █    ██  ▄▄▄       ███▄    █
  ▓██ ▒ ██▒▒████▄     ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒ ██  ▓██▒▒████▄     ██ ▀█   █
  ▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▓██  ▒██░▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒██▀▀█▄  ░██▄▄▄▄██ ▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▓▓█  ░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒
  ░██▓ ▒██▒ ▓█   ▓██▒▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒▒▒█████▓  ▓█   ▓██▒▒██░   ▓██░
  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒
    ░▒ ░ ▒░  ▒   ▒▒ ░░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░ ░░▒░ ░ ░   ▒   ▒▒ ░░ ░░   ░ ▒░
    ░░   ░   ░   ▒    ░░░ ░ ░    ░   ░ ░ ░ ░   ░  ░░░ ░ ░   ░   ▒      ░   ░ ░
     ░           ░  ░   ░              ░       ░    ░           ░  ░         ░
                                                                               '''
print(banner)
def banner_pito():
    print('''
          　　　　　▄█▀█▀█▄
　　　　　　　　▄█▀　　█　　▀█▄
　　　　　　　▄█▀　　　　　　　▀█▄
　　　　　　　█　　　　　　　　　　█
　　　　　　　█　　　　　　　　　　█
　　　　　　　▀█▄▄　　█　　　▄█▀
　　　　　　　　　█　　▄▀▄　　█
　　　　　　　　　█　▀　　　▀　█
　　　　　　　　　█　　　　　　　█
　　　　　　　　　█　　　　　　　█
　　　　　　　　　█　　　　 　　 █
　　　　　　　　　█　　　　　　　█
　　　　　　　　　█　　　　　　　█
　　　▄█▀▀█▄█　　　　　　　█▄█▀█▄
　▄█▀▀　　　　▀　　　　　　　　　　　　▀▀█
█▀　　　　　　　　　　　　　　　　　　　　　　▀█
█　　　　　　　　　　　　　　　　　　　　　　　　█
█　　　　　　　　　　　▄█▄　　　　　　　　　　█
▀█　　　　　　　　　█▀　▀█　　　　　　　　█▀
　▀█▄　　　　　　█▀　　　▀█　　　　　▄█▀
　　　▀█▄▄▄█▀　　　　　　▀█▄▄▄█▀

          ''')
nombreJug1 = input('Ingrese el nick del jugador 1: ')
nombreJug2 = input('Ingrese el nick del jugador 2: ')
# print('\n')

while(vida_juagdor1 > 0 and vida_juagdor2 > 0):
    if turno == 1:
        rand = randrange(1,21)
        #import pdb; pdb.set_trace()
        if rand > vida_juagdor2:
            vida_juagdor2 = 0
            continue
        else:
            vida_juagdor2 -= rand
        if(rand > 15):
            print("\n###### CRITICAL HIT #######")
        print("\n{} golpeo a {} por {}".format(nombreJug1,nombreJug2,rand))
        print('{} queda con {} de vida.\n'.format( nombreJug2,vida_juagdor2))
        turno = 2
        input('Presione una tecla para que {} pegue...'.format(nombreJug2))
    else:
        rand = randrange(1,21)
        # print("{} este es el rand jug 2".format(rand))
        if rand > vida_juagdor1:
            vida_juagdor1 = 0
            continue
        else:
            vida_juagdor1 -= rand
        if(rand > 15):
            print("\n###### CRITICAL HIT #######")
        print("\n{} golpeo a {} por {}".format(nombreJug2,nombreJug1,rand))
        print('{} queda con {} de vida.\n'.format( nombreJug1,vida_juagdor1))
        turno = 1
        input('Presione una tecla para que {} pegue...'.format(nombreJug1))
else:
    if vida_juagdor1 <= 0:
        print('#'*30+'\n{} es the WINNER!!!!\n'.format(nombreJug2)+'#'*30)
        banner_pito()
    elif(vida_juagdor2 <= 0):
        print('#'*30+'\n{} es the WINNER!!!!\n'.format(nombreJug1)+'#'*30)
        banner_pito()
