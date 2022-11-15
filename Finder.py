from pyautogui import moveTo, click, press, hotkey
from keyboard import write
from time import sleep


def action(site, nome, ferramenta, pesquisa):
    moveTo(77, 752)

    click(button='right')
    sleep(0.5)

    press('down')
    sleep(0.1)
    press('down')
    sleep(0.1)
    press('down')
    press('enter')

    sleep(7)
    hotkey('win', 'up')
    sleep(0.5)

    if ferramenta == 2 or ferramenta == 3:
        if pesquisa == 3 or pesquisa == 1:
            write(f'{site}/search?q={nome}', 0.05) 

        else:
            write(f'{site}/?s={nome}', 0.05)
    else:
        write(f'{site}/?s={nome}', 0.05)
            
    sleep(0.2)

    press('enter')


opcoes = input('[1] animes\n[2] Jogos\n[3] Aplicativos\n> ')
thing = int(opcoes)

if opcoes == '1':
    
    anime = input('\nNome do Anime:\n> ').replace(' ', '+').lower()

    if anime == '':
        print('\nNão tem como pesquisar "nada".\nPor favor, feche e abra o programa novamente!')
        i = input()

    else:
        site = input('\n[1] Animes Zone\n> ')
        number = int(site)

        if site == '1':
            site = 'animeszone.net'

        else:
            print('\nOpção inválida.\nPor favor, feche e abra o programa novamente!')
            i = input()

        
        action(site, anime, thing, number)

elif opcoes == '2':

    game = str(input('\nNome do jogo:\n> ')).replace(' ', '+').lower()

    if game == '':
        print('\nNão tem como pesquisar "nada".\nPor favor, feche e abra o programa novamente!')
        i = input()

    else:
        site = input('\n[1] Steam Unlocked\n[2] Br Jogos Torrent\n[3] The Pirate Jogos\n> ')
        number = int(site)

        if site == '1':
            site = 'steamunlocked.net'
            
        elif site == '2':
            site = 'brjogostorrents.com'

        elif site == '3':
            site = 'thepiratejogos.net'
            
        else:
            print('\nOpção inválida.\nPor favor, feche e abra o programa novamente!')
            i = input()

        action(site, game, thing,number)

elif opcoes == '3':
    app = str(input('\nNome do aplicativo:\n> ')).replace(' ', '+').lower()
    
    if app == '':
        print('\nNão tem como pesquisar "nada".\nPor favor, feche e abra o programa novamente!')
        i = input()

    else:
        site = input('\n[1] APK Pure\n> ')
        number = int(site)

        if site == '1':
            site = 'apkpure.com/br'

        else:
            print('\nOpção inválida.\nPor favor, feche e abra o programa novamente!')
            i = input()

        action(site, app, thing,number)

else:
    print('\nOpção inválida.\nPor favor, feche e abra o programa novamente!')
    i = input()
