from pyautogui import moveTo, click, press, hotkey
from keyboard import write
from time import sleep
from os import system

from unidecode import unidecode
from pyperclip import copy

import re
import requests

def search(search_word):
    
    dias='domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sabado'

    for c in range(0, len(dias)):

        url=f'https://animeszone.net/calendario/?semana={dias[c]}'
        html_code = requests.get(url).text

        results = re.findall(search_word, html_code)

        dia = dias[c].partition("-")

        if len(results) > 0:
            print(f'(X) {dia[0].capitalize()} *site copiado*')
            unidecode(dias[c])
            copy(f'https://animeszone.net/calendario/?semana={dias[c]}')

        else:
            print(f'( ) {dia[0].capitalize()}')

    input('\n<press enter to exit...>')

def action(site, nome, ferramenta, pesquisa):
    system('"C:\Program Files\BraveSoftware\Brave-Browser\Application/brave.exe" -incognito')
    moveTo(50, 50)

    if ferramenta == 2 or ferramenta == 3:
        if pesquisa == 3:
            write(f'{site}/search?q={nome}', 0.05) 

        else:
            write(f'{site}/?s={nome}', 0.05)

    elif ferramenta == 1:
        if pesquisa == 2:
            write(f'{site}/pesquisa?titulo={nome}')

        else:
            write(f'{site}/?s={nome}', 0.05)
            
    else:
        write(f'{site}/?s={nome}', 0.05)
            
    sleep(0.2)

    press('enter')


opcoes = input('[1] Animes\n[2] Jogos\n[3] Aplicativos\n[4] Filmes\n[5] Calendário animes\n> ')
thing = int(opcoes)

if opcoes == '1':
    
    anime = input('\nNome do Anime:\n> ').replace(' ', '+').lower()

    if anime == '':
        print('\nNão tem como pesquisar "nada".\nPor favor, feche e abra o programa novamente!')
        i = input()

    else:
        site = input('\n[1] Animes Zone\n[2] Better Anime\n[3] Anitube\n> ')
        number = int(site)

        if site == '1':
            site = 'animeszone.net'

        elif site == '2':
            site = 'betteranime.net'

        elif site == '3':
            site = 'anitube.site'

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

elif opcoes == '4':
    filme = str(input('\nNome do Filme:\n>')).replace(' ', '+').lower()

    if filme == '':
        print('\nNão tem como pesquisar "nada".\nPor favor, feche e abra o programa novamente!')
        i = input()

    else:
        site = input('\n[1] Torrent do Filmes\n>')
        number = int(site)

        if site == '1':
            site = 'torrentdofilmes.com'

        else:
            print('\nOpção inválida.\nPor favor, feche e abra o programa novamente!')
            i = input()

        action(site, filme, thing, number)

elif opcoes == '5':
    word = str(input('\nNome do Anime:\n>')).lower().replace(' ', '-')
    print()
    search(word)
            
else:
    print('\nOpção inválida.\nPor favor, feche e abra o programa novamente!')
    i = input()
