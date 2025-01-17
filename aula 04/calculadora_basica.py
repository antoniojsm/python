#calculadora basica

num1=float(input('digite um numero:'))
num2=float(input('digite outro numero:'))

print ('digite 1 para adição')
print ('digite 2 para subtração')
print ('digite 3 para multiplicação')
print ('digite 4 para divisão')

opcoes=input('digite qual calculo devo realizar:')

if (opcoes=='1'):
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é {resultado}")
elif opcoes=='2':
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é {resultado}")
elif opcoes=='3':
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é {resultado}")
else:
    resultado = num1 / num2
    print(f"O resultado de {num1} / {num2} é {resultado}")



