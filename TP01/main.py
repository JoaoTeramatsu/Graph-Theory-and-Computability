import time
from grafo import Grafo

def main():
    print("Escolha o tamanho do grafo:")
    print("1. 10 vértices")
    print("2. 100 vértices")
    print("3. 1000 vértices")
    print("4. 100000 vértices")
    
    escolha_tamanho = input("Digite o número correspondente ao tamanho: ")

    match escolha_tamanho:
        case "1":
            tamanho = 10
        case "2":
            tamanho = 100
        case "3":
            tamanho = 1000
        case "4":
            tamanho = 100000
        case _:
            print("Escolha inválida.")
            return
    g = Grafo(tamanho)

    print("Escolha o tipo de grafo:")
    print("1. Gerar grafo aleatório")
    print("2. Gerar árvore geradora mínima")
    escolha_tipo = input("Digite o número do tipo de grafo: ")

    match escolha_tipo:
        case "1":
            g.gerar_grafo_aleatorio(tamanho)
        case "2":
            g.gerar_arvore_minima(tamanho)
        case _:
            print("Escolha inválida.")
            return

    start_time = time.time()  # Captura o tempo de início
    tem_ciclos = g.verificar_ciclos()  # Chama o método para verificar ciclos
    end_time = time.time()  # Captura o tempo de término

    execution_time = (end_time - start_time) * 1e9 # converte para nanosegundos

    # Imprime os resultados
    print("O grafo contém ciclos." if tem_ciclos else "O grafo não contém ciclos.")
    print(f"Tempo de execução: {execution_time:.10f} milissegundos")
    articulacoes = g.encontrar_vertices_articulacao()
    
    # Medir o tempo de execução do método encontrar_vertices_articulacao
    start_time = time.time()  # Captura o tempo de início
    articulacoes = g.encontrar_vertices_articulacao()  # Chama o método para encontrar articulações
    end_time = time.time()  # Captura o tempo de término
    
    execution_time = (end_time - start_time) * 1e9 # converte para nanosegundos

    # Calcula o tempo de execução em milissegundos
    execution_time_articulacoes = (end_time - start_time) * 1e9  # converte para milissegundos
    print(f"Foram encontradas articulações." if articulacoes else "Não foram encontradas articulações.")
    print(f"Tempo de execução: {execution_time:.10f} milissegundos")

if __name__ == "__main__":
    main()
