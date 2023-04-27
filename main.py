# PROJETO: CRONÔMETRO EM PYTHON
# fazendo as importações necessárias
from tkinter import *
from PIL import ImageTk, Image

# minhas cores
cinza = '#5e5e5e'
cinza_escuro = '#424242'
verde = '#60be92'

# criando e configurando minha janela principal
janela = Tk()
janela.title('Cronômetro')
janela.geometry('400x160')
janela.config(bg=cinza)
janela.resizable(FALSE, FALSE)
janela.iconphoto(False, PhotoImage(file='imagens/icon.png'))

# minhas variáveis globais
global tempo_def
global tempo_temp
global limitador
global segundos_cont
global flow

# inicializando minhas variáveis globais
limitador = 5
tempo_def = '00:00:00'
segundos_cont = 0

# PARTE BACK-END
def contar():
    global tempo_def
    global tempo_temp
    global segundos_cont
    global limitador
    global flow


    if flow == True:
        # passando o valor da minha variável do tempo corrente para uma variável que guarda o tempo temporiamente e é nela que vamos fazer as operações
        tempo_temp = str(tempo_def)

        # pegando o valor dos segundos, dos minutos e das horas
        h, m, s = map(int, tempo_temp.split(':'))
        h = int(h)
        m = int(m)
        s = int(segundos_cont)

        # ATULIZAÇÕES DO TEMPO
        if (s >= limitador):
            segundos_cont = 0
            m += 1

            if m >= limitador:
                m = 0
                h += 1

        # acresentando o 0 a esquerda que é perdido no split
        s = str(0) + str(s)
        m = str(0) + str(m)
        h = str(0) + str(h)

        # passando os valores atualizadados para a nossa variável temporária
        tempo_temp = str(h[-2:]) + ':' + str(m[-2:]) + ':' + str(s[-2:])

        # mostrando o valor do tempo, JÁ ATUALIZADO, da variável do tempo temporário na tela
        lb_visor['text'] = tempo_temp

        # atualizando a variável do tempo definitivo com o valor da variável tempo temporário
        tempo_def = tempo_temp

        # chamando essa mesma função denovo
        lb_visor.after(1000, contar) # recursividade

        # atualizando os segundos
        segundos_cont += 1


# permitindo o fluxo e chamando a contagem do tempo
def start():
    global flow
    flow = True
    contar()

# interrompendo o fluxo
def pause():
    global flow
    flow = False

# resetando tudo
def restart():
    global segundos_cont
    global tempo_def

    segundos_cont = 0

    tempo_def = '00:00:00'
    lb_visor['text'] = tempo_def

# PARTE FRONT-END
# minhas imagens
icon_start = Image.open('imagens/icon-start.png')
icon_start = icon_start.resize((35, 35))
icon_start = ImageTk.PhotoImage(icon_start)

icon_pause = Image.open('imagens/icon-pause.png')
icon_pause = icon_pause.resize((35, 35))
icon_pause = ImageTk.PhotoImage(icon_pause)

icon_restart = Image.open('imagens/icon-restart.png')
icon_restart = icon_restart.resize((35, 35))
icon_restart = ImageTk.PhotoImage(icon_restart)

# labels
lb_title = Label(janela, text='cronômetro', font=('Arial 18'), bg=cinza, fg=verde)
lb_title.place(x=100, y=15)

lb_visor = Label(janela, text='00:00:00', font=('Arial 50 bold'), bg=cinza, fg=verde)
lb_visor.place(x=12, y=40)

# buttons
# botão de iniciar
bnt_start = Button(janela, text='', width=75, height=33, bg=cinza_escuro, fg=verde, font=('Arial 8 bold'), image=icon_start, bd=4, command=start)
bnt_start.place(x=300, y=10)

# botão de pausar
bnt_pause = Button(janela, text='', width=75, height=33, bg=cinza_escuro, fg=verde, font=('Arial 8 bold'), image=icon_pause, bd=4, command=pause)
bnt_pause.place(x=300, y=60)

# botão de reiniciar
bnt_restart = Button(janela, text='', width=75, height=33, bg=cinza_escuro, fg=verde, font=('Arial 8 bold'), image=icon_restart, bd=4, command=restart)
bnt_restart.place(x=300, y=110)


janela.mainloop() # loop infinito