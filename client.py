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
    return pd.read_csv('resultado.txt', header = None, sep=' ')

def write_results(df):
    df.to_csv('resultado.txt', header=None, index=None, mode='w', sep = ' ')


def max_next_move(plataforma, matriz):
    maior = 0
    idx = -1

    print("Iteração")
    for x in range(3):
        print(x)
        if matriz[plataforma][x] >= maior: #tem que garantir que as duas variáveis são do mesmo tipo!
            maior = matriz[plataforma][x]
            idx = x

    return idx

def chose_move(move):
    if move == 0:
        return 'left'

    elif move == 1:
        return 'right'

    elif move == 2:
        return 'jump'

#Return the line of the matix
def pos_matrix(bina):
    num = int(bina, 2)

    return num // 24 + num % 4

def main():

    #Declaração de Variáveis
    LOOP_ITERAIONS = 5
    LEARNING_RATE = 0.4
    DISCOUNT_FACTOR = 0.4
    reward = 0

    plataform = 0 # Você pode setar a plataforma e o giro inicial
    move = randint(0, 2)
    matriz = read_txt()
    print(matriz)
    connect_port = cn.connect(2037)
    if connect_port != 0:
        #Loop de 10000 iterações, ao final ele vai salvar o resultado final da tabela
        for _ in range(LOOP_ITERAIONS):
            next_move = max_next_move(plataform, matriz)
            print(f"Next Move: {next_move}")
            matriz[plataform][move] = matriz[plataform][move] + LEARNING_RATE * (reward + DISCOUNT_FACTOR *  -  matriz[plataform][next_move] - matriz[plataform][move])
            move = next_move
            action = chose_move(move)
            print(action)
            state, reward = cn.get_state_reward(connect_port, action)

            plataform = pos_matrix(state)

        write_results(matriz)
        connect_port.close()

if __name__=="__main__":
    main()