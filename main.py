#variaveis iniciais
salario = float(input("Digite o seu salário"))
fDesc = {0:0.0, 1: 7.5, 2:15.0, 3:22.5, 4:27.5}
fVPad = {0:0.0, 1:142.80, 2:354.80, 3:636.13, 4:869.36}

#condicionais 
if (salario < 1903.98):
    faixa = 0
elif (salario >=1903.99) and (salario <= 2826.65):
    faixa = 1
elif (salario >=2826.66) and (salario <= 3751.05):
    faixa = 2
elif (salario >= 3751.06) and (salario <= 4664.68):
    faixa = 3
else:
    faixa = 4

#calculo do IRRS
imposto = salario * (fDesc[faixa]/100)
vpad = fVPad [faixa]
imposto_pagar = imposto - vpad
liquido = salario - imposto_pagar

#mensagens 
mensagem1 = ("Bruto: %10.2f, Faixa: %d, Imposto: %5.2f" % (salario, faixa, imposto))
mensagem2 = ("Padrão: %5.2f, Pagar: %5.2f, Líquido: %5.2f" % (vpad, imposto_pagar, liquido))

print(mensagem1)
print(mensagem2)
