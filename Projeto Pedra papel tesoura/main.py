import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
#  CORES ----------------------------------------------

cor0 = "#FFFFFF"   # branco
cor1 = "#333333"   # branco
cor2 = "#fcc058"   # laranja
cor3 = "#fff873"   # valor
cor4 = "#34eb3d"   # verde
cor6 = "#fcc058"   # laranja
cor7 = "#e85151"   # vermelha

fundo = "#3b3b3b"

# CONFIGURANDO A JANELA

janela = Tk()                                 # Variável recebeu a classe Tk
janela.title('')                              # título
janela.geometry('280x300')                    # largura x altura
janela.configure(bg=fundo)                    # background: cor de fundo da nossa janela



# DIVIDINDO A JANELA

frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=cor0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


# CONFIGURANDO O FRAME DE CIMA


app_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
app_1_pontos.place(x=50, y=20)


app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
app_.place(x=125, y=20)



app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0)
app_2_linha.place(x=255, y=0)


app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('Ivy 1 bold'), bg=cor0, fg=cor0)
app_linha.place(x=0, y=95)



app_pc = Label(frame_baixo, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0)
app_pc.place(x=190, y=10)


global voce
global pc
global rondas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rondas = 5

# FUNÇÃO LÓGICA JOGO
def jogar(i):
    global rondas
    global pontos_voce
    global pontos_pc

    if rondas > 0:
        print(rondas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i

        app_pc['text'] = pc
        app_pc['fg'] = cor1

        if voce == 'Pedra' and pc == 'Pedra':
            print('Empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor3

        elif voce == 'Papel' and pc == 'Papel':
            print('Empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor3

        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor3

        elif voce == 'Pedra' and pc == 'Papel':
            print('PC venceu!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor4
            app_linha['bg'] = cor3

            pontos_pc += 10

        elif voce == 'Pedra' and pc == 'Tesoura':
            print('VC venceu!')
            app_1_linha['bg'] = cor4
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0

            pontos_voce += 10

        elif voce == 'Papel' and pc == 'Tesoura':
            print('PC venceu!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor4
            app_linha['bg'] = cor0

            pontos_pc += 10

        elif voce == 'Papel' and pc == 'Pedra':
            print('VC venceu!')
            app_1_linha['bg'] = cor4
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0

            pontos_voce += 10

        elif voce == 'Tesoura' and pc == 'Papel':
            print('VC venceu!')
            app_1_linha['bg'] = cor4
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0

            pontos_voce += 10

        elif voce == 'Tesoura' and pc == 'Pedra':
            print('PC venceu!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor4
            app_linha['bg'] = cor0

            pontos_pc += 10

        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        rondas -= 1
    else:
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        fim_do_jogo()




# FUNÇÃO INICIAR JOGO
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('imagens/pedra.png')
    icon_1 = icon_1.resize((50, 50))
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra') ,width=50, image=icon_1, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'),
                      anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('imagens/papel.png')
    icon_2 = icon_2.resize((50, 50))
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel') ,width=50, image=icon_2, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'),
                      anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=60)

    icon_3 = Image.open('imagens/tesoura.png')
    icon_3 = icon_3.resize((50, 50))
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura') ,width=50, image=icon_3, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'),
                      anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)




# FUNÇÃO FINALIZAR JOGO

def fim_do_jogo():
    global rondas
    global pontos_voce
    global pontos_pc

    pontos_voce = 0
    pontos_pc = 0
    rondas = 5

    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    jogador_voce = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    if jogador_voce > jogador_pc:
        app_vencedor = Label(frame_baixo, text="PARABÉNS, VOCÊ VENCEU!!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor4)
        app_vencedor.place(x=36, y=60)

    elif jogador_pc > jogador_voce:
        app_vencedor = Label(frame_baixo, text="VOCÊ PERDEU!!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor7)
        app_vencedor.place(x=36, y=60)

    else:
        app_vencedor = Label(frame_baixo, text="EMPATE!!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor1)
        app_vencedor.place(x=40, y=60)


    def jogar_de_novo():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()

        b_jogar_de_novo.destroy()

        iniciar_jogo()

    b_jogar_de_novo = Button(frame_baixo, command=jogar_de_novo, width=30, text='JOGAR DE NOVO', bg=fundo, fg=cor0,font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED)
    b_jogar_de_novo.place(x=5, y=151)

b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='JOGAR', bg=fundo, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED)
b_jogar.place(x=5, y=151)


janela.mainloop()