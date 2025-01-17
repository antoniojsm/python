#calculadora basica

num1=int(input('digite um numero:'))
num2=int(input('digite outro numero:'))

print ('digite 1 para adição')
print ('digite 2 para subtração')
print ('digite 3 para multiplicação')
print ('digite 4 para divisão')

opcoes=input('digite qual calculo devo realizar:')

if (opcoes=='1'):
    print(num1+num2)
elif opcoes=='2':
    print(num1-num2)
elif opcoes=='3':
    print(num1*num2)
else:
    print(num1/num2)



