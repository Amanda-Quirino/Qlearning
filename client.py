"""
- Temos que setar o learning rate, mas que 0,5 > x < 0,7 -> Valor indicado pelo monitor
    -Até 0,4 dá
- Para Discart rate, nunca muito abaixo de 0,3 nem muito acima de 0,7
- Iremos escolher a melhor ação de forma ugulosa
- Calcula a forma, atualiza esse valor na matriz resultado.txt, pega a melhor ação atual que passa a ser o current value
- 
"""
import connection as cn
import pandas as pd
from random import randint


def read_txt():
    return pd.read_fwf('resultado.txt', header = None)

def write_results(df):
    df.to_csv('resultado.txt', header=None, index=None, sep=' ', mode='w')

def max_next_move():
    pass

#Return the line of the matix
def pos_matrix(str: binary):
    num = int(binary, 2)

    return num // 24 + num % 4

def 

def main():

    #Declaração de Variáveis

    LOOP_ITERAIONS = 10000
    LEARNING_RATE = 0.4
    DISCOUNT_FACTOR = 0.4
    reward = 0

    plataform = 0 # Você pode setar a plataforma e o giro inicial
    move = randint(0, 2)
    matriz = read_txt()
    connect_port = cn.connect(2037)

    #Loop de 10000 iterações, ao final ele vai salvar o resultado final da tabela
    for x in range(LOOP_ITERAIONS):
        next_move = max_next_move(plataform, move)
        matriz[plataform][move] = matriz[plataform][move] + LEARNING_RATE * (reward + DISCOUNT_FACTOR *  - next_move - matriz[plataform][move])




if __name__=="__main__":
    main()