import numpy as np
vetor = []
vetor_antes_do_ponto = []
vetor_depois_do_ponto = []
n=0
quant=0
while True: # Conferir quando o usuário termina de digitar o numero binário
    binario = input("Digite o número binário: ")
    if binario == "": 
        break  
    vetor.append(binario)
    n=n+1 # Contando a quantidade de elementos do vetor
k=0 
num_elem=n # Número de elementos do vetor
soma_antes_total=0 # Soma total dos números antes do ponto
for i in range (n): 
    if(vetor=="."): # Verificando se existe ponto do binario 
        quant_elem_antes=i # Quantidade de elementos antes do ponto
    
        for k in range (quant_elem_antes): 
            soma_antes=vetor*np.power(2,quant_elem_antes-(i+1)) 
            soma_antes_total+=soma_antes
        
