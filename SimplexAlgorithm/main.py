import numpy as np
import simplex as sy

def main():
    decisions_variables = int(input("Quantas variaveis de decisao tem o problema: "))
    constraints = int(input ("Quantas restricoes (Exceto a restrição de não negatividade): "))
    goal = int(input("Qual o objetivo da funcao (1-Maximizar / 2-Minimizar): "))

    columns = decisions_variables+constraints+1 # Quantidade de colunas da tabela
    lines = constraints+1 # Quantidade de linhas da tabela

    print("Entre com a Funcao(z) na forma canonica:")
    
    # Preenchendo a função objetivo z
    z = np.zeros(columns)
    for i in range(0, decisions_variables):
        z[i] = (int(input('X' + str(i+1) + ': ')))

    # Preenchendo as restrições e montando a primeira tabela
    table = np.zeros((lines, columns))

    for i in range(0, columns):
        if z[i] != 0:
            table[0][i] = z[i]*-1

    for i in range(1, lines):
        print("Restrição " + str(i)+ " (forma canonica):")
        option = 0

        for j in range(0, columns):  
            # Se estiver entrando com as X da restrição
            if j < decisions_variables:
                table[i][j] = (input('X' + str(j+1) + ': '))

            # Se estiver entrando com o final da restrição
            elif j == columns-1:
                if option == 1:
                    table[i][j] = (input('<= '))
                else:
                    table[i][j] = (input('>= '))

            # Coloca 1 ou -1 automaticamente
            elif j ==  i+(decisions_variables)-1:
                option = int(input("1 - <= / 2 - >= : "))
                if option == 1:     
                    table[i][i+(decisions_variables)-1] = 1
                else:
                    table[i][i+(decisions_variables)-1] = -1

    sy.simplex(table, lines, columns, decisions_variables, constraints) # Chamando a função para realizar o método simplex
    
if __name__ == "__main__":
    main()