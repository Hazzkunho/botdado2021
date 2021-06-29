import random

#Função de entrada dos dados
def entrada():
        #Quantidade de dados e faces
        dados_txt = input("Por favor, diga a quantidade de dados: ")
        dados_int = int(dados_txt)

        faces_txt = input("Agora, informe a quantidade de faces: ")
        faces_int = int(faces_txt)

        return  dados_int, faces_int

# Programa Principal
dados, faces = entrada()

# Saída dos dados: Valor de cada dado individual e a soma no final.
somatorio = 0
for rodada in range(1, dados + 1):
        aleatorio = random.randint(1,faces)
        somatorio = somatorio + aleatorio
        print("Rodada", rodada, ":", aleatorio)
print("--0--")
print("Somatorio", somatorio)
