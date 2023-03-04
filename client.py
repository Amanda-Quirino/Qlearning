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
    maior = matriz[0][plataforma]
    idx = 0

    for x in range(1,3):
        if matriz[x][plataforma] >= maior: #tem que garantir que as duas variáveis são do mesmo tipo!
            maior = matriz[x][plataforma]
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
    print(bina)
    plataform = int(bina[2:7],2)
    direction = int(bina[8:10],2)
    print(f"plataforma: {plataform}")
    return ((4 * plataform) + direction) +1

def main():

    #Declaração de Variáveis
    LOOP_ITERAIONS = 1000
    LEARNING_RATE = 0.4
    DISCOUNT_FACTOR = 0.4
    reward = 0
    
    plataform = 41 # Você pode setar a plataforma e o giro inicial
    move = randint(0, 2)
    matriz = read_txt()
    print(matriz)
    connect_port = cn.connect(2037)
    if connect_port != 0:
        #Loop de x iterações, ao final ele vai salvar o resultado final da tabela
        for _ in range(LOOP_ITERAIONS):
            next_move = max_next_move(plataform, matriz)
            print(f"Next Move: {next_move}")
            matriz[move][plataform] = matriz[move][plataform] + LEARNING_RATE * (reward + DISCOUNT_FACTOR *  -  matriz[next_move][plataform] - matriz[move][plataform])
            action = chose_move(move)
            print(action)
            state, reward = cn.get_state_reward(connect_port, action)
            move = next_move
            plataform = pos_matrix(state)
            print(plataform)

        write_results(matriz)
        connect_port.close()

if __name__=="__main__":
    main()