vc = float(input("Digite o valor da casa que deseja financiar: "))
sal = float(input("Digite quanto você ganha por mês: "))
tmp = int(input("digite em quantos meses você deseja parcelar: "))
a = vc / tmp
limite = sal * 30 / 100
print(f"Casa no valor de: R${vc:.2f} com salario de: R${sal:.2f} e parcelas de: {tmp} meses!")
if limite < a:
    print("Emprestimo não aprovado pois excedeu o valor de 30% do salario")
else:
    print(f"Emprestimo aprovado no valor de R${a:.2f}  por mês, em {tmp} parcelas ")