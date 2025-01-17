# collections, lists e tuples

familia=['antonio','pedro','maria','ricardo']
        #    0        1       2        3
print(familia) #imprimir a lista 
print(familia[0]) #primeira pessoa da lista
print(familia[1:3])#retorna as pessoas apartir de 1, excluindo o 3

familia[1]='matheus' #troca o nome de pedro para matheus

familia.extend(['francisco','clara']) #adiciona mais 2 nomes a familia

familia.append('jupi') #adiciona apenas um valor a lista

familia.insert(1,'jupi')#ele vira o valor numero 1

familia.remove('jupi') #remove o nome jupi

idade_familia=[34,24,13,11,4]
print(idade_familia)
idade_familia.sort()#ordenar em ordem crescente
print(idade_familia)

familia.sort() #ordenar strings em ordem alfabetica
print (familia)

idade_familia.reverse()#inverter os numeros
print(idade_familia)

familia.reverse()#inverte os nomes
print(familia)

#listas

coordenadas=[-49,-36]
coordenadas.pop()
print(coordenadas)

#tuples
coordenadas=(-49,-36)#usado para não alterar nem um valor



