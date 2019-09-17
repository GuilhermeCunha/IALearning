import matplotlib.pyplot as plt
import numpy as np
import random

max_int = 20

# entradas
x = [[0,0,1],
     [0,1,1],
     [1,0,1],
     [1,1,1]]

# quantos itens tem o vetor x (4)
tamanho_x = len(x)

# quantos itens estão em cada posicao do vetor x
qtde_itens_x = len(x[0])

# pesos (sinapses)
w = [0.5,0.6,-0.3]

# quantos itens tem o vetor w (3)
tamanho_w = len(w)

# respostas desejadas
d = [0,0,0,1]

# taxa de aprendizado (n)
taxa_aprendizado = 0.1

#saida
y = 0

# resposta = acerto ou falha
resposta = ""

# soma
u = 0

print("Treinando")

# inicio do algoritmo
for k in range(0,max_int):
    acertos = 0    
    alternancia_peso = 0;
    
    print("pesos:")
    for j in range (0,tamanho_w):
        print(str(w[j]) + " - " , end="")
    
    print("\nÉpoca "+str(k)+"-------------------------")
    
    for t in range(0,tamanho_x):        
        u = 0

        for j in range(0,qtde_itens_x):
            u += x[t][j] * w[j]

        # funcao de saida
        if u >= 0:
            y = 1       
        else:
            y = 0

        print(str(x[t][0]) + "." + str(x[t][1]))
        
        if y == d[t]:
            resposta = "acerto"
            acertos += 1        
            print(resposta + " >>> u = "+str(u)+ ", y = "+ str(y))   
        else:
            resposta = "erro"        
            print(resposta + " >>> u = "+str(u)+ ", y = "+ str(y))
            
            for j in range (0,tamanho_w):
                if(x[t][j] == 1):
                    w[j] = w[j] - taxa_aprendizado
                    
           
    if acertos == tamanho_x:
        print("\nFuncionalidade aprendida com "+str(k)+" épocas")
        print("\nPesos encontrados =============== ")
        for j in range (0,tamanho_w):
            print(w[j])
        break;
    

    
    print("")

#pontos no gráfico
for t in range(0,tamanho_x):  
    plt.scatter(x[t][0], x[t][1])
    
x1 = (((-1)*w[2])/w[0])
x2 = (((-1)*w[2])/w[1])
print(str(x1) + "," + str(x2))

pontos = [[0,x1],[x2,0]]

z = np.polyfit(pontos[0],pontos[1],1)
p = np.poly1d(z)
print("Best fit polinomial equation: ",p)
# Generates plot
plt.plot(pontos, p(pontos), '-')

#plt.axis([0, 2, 0, 2])
plt.show()
print("Finalizado")