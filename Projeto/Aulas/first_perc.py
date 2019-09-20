import random

data = [
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [1,1,1]
]
x = []
y = []
bias = 1
for i in data:
    d = i[:2] 
    d.append(bias)
    x.append(d)
    y.append(i[2])

# print(x)
print(y[3])

epochs = 5

w = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
#w = [0.5,0.6,-0.3]
tx_apr = 0.05
for epoch in range(epochs):
    erros = 0
    acertos = 0
    for linha in range(0, len(x)):
        sum = 0
        saida = 0
        for coluna in range(len(x[0])):
            sum += x[linha][coluna]*w[coluna]
        
        if(sum > 0):
            saida = 1
        else:
            saida = 0

        if saida == y[linha]:
            print("ACERTOU")
            acertos += 1
        else:
            erros += 1
            print("ERROU")
            print("ESPERADO: ",y[linha])
            print("SOMA = ", sum)
            for coluna in range(0, len(w)):
                erro = y[coluna] - sum
                print("{0} = {0} + ({1} * ({2} * {3}))".format(w[coluna], tx_apr, erro, x[linha][coluna]))
                w[coluna] = w[coluna] + (tx_apr * (erro * x[linha][coluna]))
    print("Epoca: ", epoch)
    if(acertos == len(x)):
        print("Terminado - Acertou todas")
        break
    else:
        print("Não perfeita: " , acertos)