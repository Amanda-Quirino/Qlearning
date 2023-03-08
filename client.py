import connection as cn
import pandas as pd
from random import randint


def read_txt():
    #Leitura do arquivo txt
    return pd.read_csv('resultado.txt', header = None, sep=' ')

def write_results(df):
    #Escrita no arquivo txt dos resultados
    df.to_csv('resultado.txt', header=None, index=None, mode='w', sep = ' ')

#Função responsável por pergar o melhor próximo movimento
def max_next_move(plataforma, matriz):
    maior = -9999
    idx = -1

    for x in range(3):
        if matriz[x][plataforma] >= maior: #tem que garantir que as duas variáveis são do mesmo tipo!
            maior = matriz[x][plataforma]
            idx = x

    return idx

#Função responsável por retornar a string do movimento que será passado para o jogo
def chose_move(move):
    if move == 0:
        return 'left'

    elif move == 1:
        return 'right'

    elif move == 2:
        return 'jump'

#Retorna a linha da matriz
def pos_matrix(bina):
    print(bina)
    plataform = int(bina[2:7],2)
    direction = int(bina[7:9],2)
    print(f"plataform: {plataform}")
    print(f"Direction: {direction}")
    return ((4 * plataform) + direction)

def main():

    #Declaração de Variáveis
    LOOP_ITERATIONS = 100
    LEARNING_RATE = 0.6
    DISCOUNT_FACTOR = 0.5
    reward = 0
    victory = 0
    next_move = 0
    next_plataform = 0

    # Você pode setar a plataforma e o giro inicial
    plataform = 0
    move = 2

    matriz = read_txt()
   
    connect_port = cn.connect(2037)
    if connect_port != 0:
        #Loop de x iterações, ao final ele vai salvar o resultado final da tabela
        for x in range(LOOP_ITERATIONS):
            print(f"\n\nPrint iteração {x + 1}")

            #realiza ação
            action = chose_move(move)
            print("Movimento: ", action)
            state, reward = cn.get_state_reward(connect_port, action)

            next_plataform = pos_matrix(state) #Pega a nova plataforma
            if reward == 300:
                victory += 1

            #Escolhe a acção da próxima jogada
            next_move = max_next_move(next_plataform, matriz) 
            #Algoritmo QLearning
            matriz[move][plataform] = matriz[move][plataform] + LEARNING_RATE * (reward + DISCOUNT_FACTOR * matriz[next_move][next_plataform] - matriz[move][plataform])
            move = next_move #Atualiza o move  e o plataform
            plataform = next_plataform
            print("Pos Martriz: ", plataform)

 
        print("victories: ", victory)
        write_results(matriz)
        connect_port.close()

if __name__=="__main__":
    main()