from rich import print
from rich.table import Table

canais = '12345'
str_canais = ''
for canal in list(canais):
    canal_escolhido:int = 1
    str_canais += ' '
    if canal_escolhido == int(canais[canal_escolhido-1]):
        str_canais += '[on white]'
        str_canais += f'{canais[canal_escolhido-1]}'
        str_canais += '[/]'
    else:
        str_canais += canal
    print(canal)
    str_canais += ' ' 
print(str_canais)
str_canais = ''
for canal in list(canais):
    canal_escolhido = 2
    str_canais += ' '
    if canal_escolhido == int(canais[canal_escolhido-1]):
        str_canais += '[on white]'
        str_canais += f'{canais[canal_escolhido-1]}'
        str_canais += '[/]'
    else:
        str_canais += canal
    str_canais +=  ' ' 
print(str_canais)





