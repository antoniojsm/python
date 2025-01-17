#funcões

def big_mac():
    print('sanduiche big mac') #função Big Mac
 
 
print('inicio')
big_mac() #imprimir a função
print('fim')
    
def fazer_big_mac(nome): #função com parametro
    print(f'sanduiche big mac {nome}')#imprimir a função
       
fazer_big_mac('antoniojose') #dados da função
fazer_big_mac('mariana')

#função combo
def fazer_batata(tamanho): 
    print(f'batata{tamanho}')
        
        
        
def preparar_refrigerante(tipo,tamanho):
        print(f'{tipo} {tamanho}')
        
        
fazer_big_mac('antonio')
fazer_batata ('grande')
preparar_refrigerante('coca','media')
        
def fazer_combo_big_mac (nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)
    
fazer_combo_big_mac('antonio','grande','coca','media')
    
    
    