import PySimpleGUI as sg
from random import randint


def tela_inicial():
    layout = [
        [sg.Text('\n\t TELA DE LOGIN\t')],
        [sg.Text('USUÁRIO')],
        [sg.Input(key='usuario')],
        [sg.Text('SENHA')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Button('entrar')],
        [sg.Text('', key='msg')]
    ]
    return sg.Window('login', layout=layout, finalize=True)


telaInicial = tela_inicial()

while True:
    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break
    senha_correta = '123456789'
    usuario_correto = 'francimar'
    usuario_digitado = valores['usuario']
    senha_digitada = valores['senha']
    if window == telaInicial and eventos == 'entrar':
        if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
            window['msg'].update('login feito com sucesso')
        else:
            window['msg'].update('usuário ou senha incorreto')
