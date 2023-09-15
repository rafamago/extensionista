from tkinter import *
import tkinter as tk

class Application:
    def __init__(self, master=None):
      self.widget = Frame(master)
      self.widget.pack()
      texto1 = self.msg = Label(self.widget, text="Olá! Bem vindo ao projeto: Como tornar o uso da água mais sustentável no dia a dia.\nNesse programa é possível saber se você está consumindo água dentro da média de uso por pessoa ou com desperdícios.\nAlém de receber dicas de como tornar o uso mais sustentável e saber um pouco mais sobre os riscos do uso exagerado da água.\nVocê sabia, que baseado nos dados da ONU, a média diária de uso de água de forma racional por pessoa é de 110 litros?\nPorém aqui no Brasil utilizamos em média 200 litros por pessoa diariamente, um dos motivos que ocasiona a crise hídrica.\nA média máxima mensal de uso é de 3.410 litros por pessoa, você sabe como calcular a sua? \nIdentificando o número da medição que consta na sua última conta de água, subtraindo pela medição da conta atual, você irá saber a quantidade gasta mensalmente.\nAqui vai algumas dicas de como racionar mais o uso da água:\nDica 1: Mantenha a torneira fechada ao escovar os dentes, fazer a barba e ao ensaboar a louça. Ao escovar os dentes com ela aberta, você gasta cerca de 13,5 litros de água em apenas dois minutos. \nDica 2: Tome banhos curtos, cinco minutos são suficientes para fazer a limpeza do corpo e, enquanto se ensaboa, o registro deve ser fechado. Isso gera uma economia de até 30 mil litros no ano.\nDica 3: Só ligue a lava-roupas quando estiver cheia, pois isso evita o desperdício. Espere juntar uma quantidade de roupas suficiente para encher a máquina.\nDica 4: Use a vassoura para limpar o quintal, a calçada, uma mangueira ligada por 15 minutos gasta 280 litros de água. \nDica 5: Use um balde e um pano para limpar o carro.\nAgora você deve se perguntar, por que é tão importante fazer uso da água de forma racional?\nEstamos vivendo uma crise hídrica onde o desperdício de água, o desmatamento e o aquecimento global, estão contribuindo para o dia que irá esgotar toda água do planeta \nE se quisermos que exista um futuro para as próximas gerações, precisamos fazer nossa parte e usar de forma racional sem desperdícios \nEntão é muito importante espalhar essa informação pois o conhecimento é a chave, se cada um fizer sua parte já contribui para um futuro melhor para a próxima geração e para a nossa! \n", font=("Georgia",10), bg="#F5F5F5")
      self.msg.pack ()
root = Tk()
root.title("Projeto: Como tornar o uso da água mais sustentável no dia a dia")
Application(root)

imagem = tk.PhotoImage(file="conta.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.pack()


janela = Tk()
janela.title("Cálculo do uso mensal")

def calcular():
    Antigafatura = float(valor_antigo.get())
    Atualfatura = int(valor_atual.get())
   

    #Cálculos
    Valor1 = (Atualfatura - Antigafatura)
    Valor2 = (Valor1 * 1000)

    #Imprimir resultado
    resultado.config(text='A quantidade utilizada no mês foi (em litros) : {:.0f}'.format(Valor2))
# Adicionar as caixas de entrada e o botão
Label(janela, text="Insira o número no medidor da fatura passada (em m³):").grid(row=0, column=0)
valor_antigo = Entry(janela)
valor_antigo.grid(row=0, column=1)

Label(janela, text="Insira o número no medidor da fatura atual (em m³):").grid(row=1, column=0)
valor_atual = Entry(janela)
valor_atual.grid(row=1, column=1)

Button(janela, text="Fazer o Cálculo", command=calcular).grid(row=2, column=0)
# Adicionar o resultado
resultado = Label(janela)
resultado.grid(row=3, column=0)
root.mainloop()
